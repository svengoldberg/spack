# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Damaris(CMakePackage):
    """Damaris is a middleware for I/O and in situ analytics
    targeting large-scale, MPI-based HPC simulations."""

    homepage = "https://project.inria.fr/damaris/"
    git = "https://gitlab.inria.fr/Damaris/damaris.git"
    maintainers("jcbowden")

    version("master", branch="master")
    version("1.6.0", tag="v1.6.0", commit="1fe4c61cce03babd24315b8e6156f226baac97a2")
    version("1.5.0", tag="v1.5.0", commit="68206a696ad430aa8426ca370501aa71914fbc87")
    version("1.3.3", tag="v1.3.3", commit="f1c473507c080738f7092f6a7d72deb938ade786")
    version("1.3.2", tag="v1.3.2", commit="38b50664523e56900809a19f0cf52fc0ab5dca53")
    version("1.3.1", tag="v1.3.1", commit="6cee3690fa7d387acc8f5f650a7b019e13b90284")

    variant("fortran", default=True, description="Enables Fortran support")
    variant("hdf5", default=False, description="Enables the HDF5 storage plugin")
    variant("static", default=False, description="Builds a static version of the library")
    variant("catalyst", default=False, description="Enables the Catalyst visualization plugin")
    variant("visit", default=False, description="Enables the VisIt visualization plugin")
    variant(
        "examples",
        default=False,
        description="Enables compilation and installation of the examples code",
    )
    variant("docs", default=False, description="Enables the building of dOxygen documentation")
    variant(
        "python",
        default=False,
        description="Enables building of Python enabled Damaris library - "
        "boost::python boost::numpy needed",
    )

    depends_on("mpi")
    depends_on("cmake@3.18.0:", type=("build"))
    depends_on(
        "boost"
        "+exception+locale+system+serialization+chrono+atomic"
        "+container+regex+thread+log+filesystem+date_time"
        "@1.67:"
    )
    depends_on("xsd")
    depends_on("xerces-c")
    depends_on("hdf5@1.8.20:", when="+hdf5")
    depends_on("paraview+python", when="+catalyst")
    depends_on("visit+mpi", when="+visit")
    depends_on("boost+thread+log+filesystem+date_time+python+numpy @1.67:", when="+python")

    def cmake_args(self):
        args = []
        if not self.spec.variants["static"].value:
            args.extend(["-DBUILD_SHARED_LIBS=ON"])

        args.extend(["-DCMAKE_CXX_COMPILER=%s" % self.spec["mpi"].mpicxx])
        args.extend(["-DCMAKE_C_COMPILER=%s" % self.spec["mpi"].mpicc])
        args.extend(["-DBOOST_ROOT=%s" % self.spec["boost"].prefix])
        args.extend(["-DXercesC_ROOT=%s" % self.spec["xerces-c"].prefix])
        args.extend(["-DXSD_ROOT=%s" % self.spec["xsd"].prefix])

        if self.spec.variants["fortran"].value:
            args.extend(["-DCMAKE_Fortran_COMPILER=%s" % self.spec["mpi"].mpifc])
            args.extend(["-DENABLE_FORTRAN:BOOL=ON"])

        if self.spec.variants["hdf5"].value:
            args.extend(["-DENABLE_HDF5:BOOL=ON"])
            args.extend(["-DHDF5_ROOT:PATH=%s" % self.spec["hdf5"].prefix])

        if self.spec.variants["catalyst"].value:
            args.extend(["-DENABLE_CATALYST:BOOL=ON"])
            args.extend(["-DParaView_ROOT:PATH=%s" % self.spec["catalyst"].prefix])
        if self.spec.variants["examples"].value:
            args.extend(["-DENABLE_EXAMPLES:BOOL=ON"])

        if self.spec.variants["docs"].value:
            args.extend(["-DENABLE_DOCS:BOOL=ON"])

        if self.spec.variants["python"].value:
            args.extend(["-DENABLE_PYTHON:BOOL=ON"])

        if self.spec.variants["visit"].value:
            args.extend(["-DENABLE_VISIT:BOOL=ON"])
            args.extend(["-DVisIt_ROOT:PATH=%s" % self.spec["visit"].prefix])
        return args
