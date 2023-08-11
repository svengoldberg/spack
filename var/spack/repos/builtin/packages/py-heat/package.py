# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHeat(PythonPackage):
    """Heat is a flexible and seamless open-source software for high performance data analytics
    and machine learning. It provides highly optimized algorithms and data structures for tensor
    computations using CPUs, GPUs and distributed cluster systems on top of MPI."""

    homepage = "https://github.com/helmholtz-analytics/heat/"
    url = "https://github.com/helmholtz-analytics/heat/archive/refs/tags/v1.3.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("1.3.0", sha256="2e66e82df87431075be633bc921a4953dd258dfa91ed31283c964bcb3dea1ffc")

    depends_on("py-mpi4py@3:", type=("build", "run"))
    depends_on("py-numpy@1.2:", type=("build", "run"))
    depends_on("py-torch@1.8:2.0.1", type=("build", "run"))
    depends_on("py-scipy@0.14:", type=("build", "run"))
    depends_on("py-pillow@6:", type=("build", "run"))
    depends_on("py-torchvision@0.8:", type=("build", "run"))

    variant("docutils", default=False)
    variant("hdf5", default=False)
    variant("netcdf", default=False)
    variant("dev", default=False)
    variant("examples", default=False)

    depends_on("py-docutils@0.16:", when="+docutils", type=("link"))
    depends_on("py-h5py@2.8.0:", when="+hdf5", type=("link"))
    depends_on("py-netcdf4@1.5.6:", when="+netcdf", type=("link"))
    depends_on("py-pre-commit@1.18.3:", when="+dev", type=("link"))
    depends_on("py-scikit-learn@0.24.0:", when="+examples", type=("link"))
    depends_on("py-matplotlib@3.1.0:", when="+examples", type=("link"))

    def install_options(self, spec, prefix):
        options = []

        if "+docutils" in spec:
            options.append("docutils")
        if "+hdf5" in spec:
            options.append("hdf5")
        if "+netcdf" in spec:
            options.append("netcdf")
        if "+dev" in spec:
            options.append("dev")
        if "+examples" in spec:
            options.append("examples")

        return options
