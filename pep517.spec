#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pep517
Version  : 0.9.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/31/65/399b2e85e1ee5e34d797643b1d1ce3ec3f2b612e0680d6b7b455c24cb7a7/pep517-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/65/399b2e85e1ee5e34d797643b1d1ce3ec3f2b612e0680d6b7b455c24cb7a7/pep517-0.9.1.tar.gz
Summary  : Wrappers to build Python packages using PEP 517 hooks
Group    : Development/Tools
License  : MIT
Requires: pep517-license = %{version}-%{release}
Requires: pep517-python = %{version}-%{release}
Requires: pep517-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
API to call PEP 517 hooks
=========================
`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ specifies a standard
API for systems which build Python packages.

%package license
Summary: license components for the pep517 package.
Group: Default

%description license
license components for the pep517 package.


%package python
Summary: python components for the pep517 package.
Group: Default
Requires: pep517-python3 = %{version}-%{release}

%description python
python components for the pep517 package.


%package python3
Summary: python3 components for the pep517 package.
Group: Default
Requires: python3-core
Provides: pypi(pep517)
Requires: pypi(toml)

%description python3
python3 components for the pep517 package.


%prep
%setup -q -n pep517-0.9.1
cd %{_builddir}/pep517-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603119475
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pep517
cp %{_builddir}/pep517-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pep517-0.9.1/tests/samples/pkg1/pkg1-0.5.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pep517-0.9.1/tests/samples/pkg2/pkg2-0.5.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
