from flask import Flask, render_template, request, send_from_directory
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import os

app = Flask(__name__)

# Load ward boundaries once
WARD_DATA = gpd.read_file("ward_polygon.geojson")
WARD_DATA = WARD_DATA[["statename", "lganame", "wardname", "geometry"]]

@app.route("/", methods=["GET", "POST"])
def index():
    states = sorted(WARD_DATA['statename'].unique())
    selected_state = request.form.get("state")
    selected_lgas = request.form.getlist("lga")
    map_filename = None

    lgas = sorted(WARD_DATA[WARD_DATA['statename'] == selected_state]['lganame'].unique()) if selected_state else []

    if request.method == "POST" and selected_state and selected_lgas:
        map_filename = generate_map(selected_state, selected_lgas)

    return render_template("index.html", states=states, lgas=lgas,
                           selected_state=selected_state,
                           selected_lgas=selected_lgas,
                           map_filename=map_filename)

def generate_map(state, lgas):
    filtered = WARD_DATA[(WARD_DATA['statename'] == state) & (WARD_DATA['lganame'].isin(lgas))]
    gdf = gpd.GeoDataFrame(filtered, geometry="geometry")
    gdf.set_crs(epsg=4326, inplace=True)
    gdf = gdf.to_crs(epsg=3857)

    fig, ax = plt.subplots(figsize=(20, 15))
    gdf.plot(ax=ax, edgecolor="black", cmap="Set2", alpha=0.6)

    for _, row in gdf.iterrows():
        ax.text(row.geometry.centroid.x, row.geometry.centroid.y, row.wardname, fontsize=8, ha="center")

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    safe_name = "_".join([l.replace("/", "-") for l in lgas])
    output_dir = "static/maps"
    os.makedirs(output_dir, exist_ok=True)

    for ext in ["png", "pdf", "svg"]:
        plt.savefig(f"{output_dir}/{safe_name}_wards_map.{ext}", format=ext)

    plt.close(fig)
    return f"{safe_name}_wards_map.png"

@app.route("/static/maps/<filename>")
def serve_map(filename):
    return send_from_directory("static/maps", filename)

if __name__ == "__main__":
    app.run(debug=True)
