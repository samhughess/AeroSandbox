import aerosandbox as asb
from aerosandbox.aerodynamics.aero_3D.test_aero_3D.geometries.conventional import airplane

analysis = asb.AeroBuildup(
    airplane=airplane,
    op_point=asb.OperatingPoint(
        atmosphere=asb.Atmosphere(altitude=0),
        velocity=10,  # m/s
        alpha=5,  # In degrees
        beta=0,  # In degrees
        p=0,  # About the body x-axis, in rad/sec
        q=0,  # About the body y-axis, in rad/sec
        r=0,  # About the body z-axis, in rad/sec
    ),
)
