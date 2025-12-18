from .scattering1d.frontend.torch_frontend import ScatteringTorch1D as Scattering1D
from .scattering1d.frontend.torch_frontend import (
    TimeFrequencyScatteringTorch as TimeFrequencyScattering,
)
from .scattering2d.frontend.torch_frontend import ScatteringTorch2D as Scattering2D
from .scattering3d.frontend.torch_frontend import (
    HarmonicScatteringTorch3D as HarmonicScattering3D,
)

Scattering1D.__module__ = "kymatio.torch"
Scattering1D.__name__ = "Scattering1D"

TimeFrequencyScattering.__module__ = "kymatio.torch"
TimeFrequencyScattering.__name__ = "TimeFrequencyScattering"

TimeFrequencyScattering1D = TimeFrequencyScattering
TimeFrequencyScattering1D.__module__ = "kymatio.torch"
TimeFrequencyScattering1D.__name__ = "TimeFrequencyScattering1D"

Scattering2D.__module__ = "kymatio.torch"
Scattering2D.__name__ = "Scattering2D"

HarmonicScattering3D.__module__ = "kymatio.torch"
HarmonicScattering3D.__name__ = "HarmonicScattering3D"

__all__ = [
    "Scattering1D",
    "TimeFrequencyScattering",
    "TimeFrequencyScattering1D",
    "Scattering2D",
    "HarmonicScattering3D",
]
