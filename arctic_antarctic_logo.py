import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.patches import Circle
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def _make_polar_logo(
    filename,
    proj,
    extent,
    dpi=600,
    ocean_colour="white",
    land_colour="black",
    border_colour="black",
    border_width=8,
    fill_ocean=False,
    fill_lakes=False
):
    fig = plt.figure(figsize=(4, 4), dpi=dpi)
    fig.patch.set_alpha(0.0)     # make background transparent
    # fig.patch.set_facecolor(ocean_colour) # or set background ocean_colour


    ax = plt.axes(projection=proj)
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    ax.set_axis_off()

    # Optionally fill ocean (inside circle) before land.
    # Using a circle patch ensures a clean circular edge under the border.
    if fill_ocean:
        ocean_circle = Circle(
            (0.5, 0.5),
            0.5,
            transform=ax.transAxes,
            facecolor=ocean_colour,
            edgecolor="none",
            zorder=0.5
        )
        ax.add_patch(ocean_circle)

    # Add land with explicit zorder to ensure it draws over ocean circle
    ax.add_feature(
        cfeature.LAND.with_scale("110m"),
        facecolor=land_colour,
        edgecolor="none",
        zorder=1
    )

    # Optionally color lakes same as ocean.
    if fill_lakes:
        ax.add_feature(
            cfeature.LAKES.with_scale("110m"),
            facecolor=ocean_colour,
            edgecolor="none",
            zorder=2
        )

    # Create circular mask
    theta = np.linspace(0, 2 * np.pi, 500)
    circle_xy = np.column_stack([np.sin(theta), np.cos(theta)]) * 0.5 + 0.5
    circle = mpath.Path(circle_xy)

    # Clip map to circle
    ax.set_boundary(circle, transform=ax.transAxes)

    # ---- Add circular border ----
    border = Circle(
        (0.5, 0.5),
        0.5,                     # radius
        transform=ax.transAxes,
        fill=False,
        lw=border_width,
        edgecolor=border_colour
    )
    ax.add_patch(border)

    # Save output
    plt.savefig(
        filename,
        bbox_inches="tight",
        pad_inches=0,
        # facecolor=fig.get_facecolor()
        transparent=True
    )
    plt.close(fig)
    print(f"Saved: {filename}")


def make_arctic_logo(
    filename="arctic_logo.png",
    **kwargs
):
    _make_polar_logo(
        filename=filename,
        proj=ccrs.NorthPolarStereo(),
        extent=[-180, 180, 60, 90],
        **kwargs
    )


def make_antarctic_logo(
    filename="antarctic_logo.png",
    **kwargs
):
    _make_polar_logo(
        filename=filename,
        proj=ccrs.SouthPolarStereo(),
        extent=[-180, 180, -90, -60],
        **kwargs
    )


if __name__ == "__main__":
    make_arctic_logo()
    make_antarctic_logo()
