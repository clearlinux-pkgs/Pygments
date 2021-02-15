#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pygments
Version  : 2.8.0
Release  : 69
URL      : https://files.pythonhosted.org/packages/19/d0/dec5604a275b19b0ebd2b9c43730ce39549c8cd8602043eaf40c541a7256/Pygments-2.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/d0/dec5604a275b19b0ebd2b9c43730ce39549c8cd8602043eaf40c541a7256/Pygments-2.8.0.tar.gz
Summary  : Pygments is a syntax highlighting package written in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Pygments-bin = %{version}-%{release}
Requires: Pygments-license = %{version}-%{release}
Requires: Pygments-python = %{version}-%{release}
Requires: Pygments-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-qmake
BuildRequires : nose

%description
~~~~~~~~
        
        Pygments is a syntax highlighting package written in Python.
        
        It is a generic syntax highlighter suitable for use in code hosting, forums,
        wikis or other applications that need to prettify source code.  Highlights

%package bin
Summary: bin components for the Pygments package.
Group: Binaries
Requires: Pygments-license = %{version}-%{release}

%description bin
bin components for the Pygments package.


%package license
Summary: license components for the Pygments package.
Group: Default

%description license
license components for the Pygments package.


%package python
Summary: python components for the Pygments package.
Group: Default
Requires: Pygments-python3 = %{version}-%{release}
Provides: pygments-python

%description python
python components for the Pygments package.


%package python3
Summary: python3 components for the Pygments package.
Group: Default
Requires: python3-core
Provides: pypi(pygments)

%description python3
python3 components for the Pygments package.


%prep
%setup -q -n Pygments-2.8.0
cd %{_builddir}/Pygments-2.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613411131
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Pygments
cp %{_builddir}/Pygments-2.8.0/LICENSE %{buildroot}/usr/share/package-licenses/Pygments/0c9b9b4787b4a052032ee71b856e9a8d37a13ea3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pygmentize

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Pygments/0c9b9b4787b4a052032ee71b856e9a8d37a13ea3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
