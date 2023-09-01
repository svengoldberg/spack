# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install memilio
#
# You can edit this file again by typing:
#
#     spack edit memilio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Memilio(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/DLR-SC/memilio"
    url = "https://github.com/DLR-SC/memilio.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add proper versions here.
    version("0.7", git="https://github.com/DLR-SC/memilio.git", branch="main")

    variant("mpi", default=False, description="Build memilio with MPI.")
    variant("hdf5", default=False, description="Build memilio with HDF5.")
    variant("jsoncpp", default=False, description="Build memilio with JsonCpp")

    # FIXME: Add dependencies if required.
    depends_on("cmake", type="build")
    depends_on("spdlog@1.11.0:")
    depends_on("eigen@3.3.9:")
    depends_on("jsoncpp@1.9.5:")
    depends_on("mpi", when="+mpi")
    depends_on("hdf5~mpi@1.12.0:", when="~mpi+hdf5")
    depends_on("hdf5+mpi@1.12.0:", when="+mpi+hdf5")
    # TODO: Up to now, Boost (besides others) is used as bundled package from the repo
    # In future, spack packages should be used to avoid different versions, in case, the package is loaded additionally elsewhere

    root_cmakelists_dir = "cpp"

    #build_directoy = "build"

    def cmake_args(self):
        args = []
        if "+mpi" in self.spec:
            args.append("-DMEMILIO_ENABLE_MPI=ON")
        return args
