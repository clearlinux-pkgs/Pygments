#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pygments
Version  : 2.7.1
Release  : 62
URL      : https://files.pythonhosted.org/packages/e2/07/25bd93c9c0175adfa5fb1513a20b25e7dd6c9a67c155e19b11b5f3662104/Pygments-2.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/07/25bd93c9c0175adfa5fb1513a20b25e7dd6c9a67c155e19b11b5f3662104/Pygments-2.7.1.tar.gz
Summary  : Pygments is a syntax highlighting package written in Python.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Pygments-bin = %{version}-%{release}
Requires: Pygments-license = %{version}-%{release}
Requires: Pygments-python = %{version}-%{release}
Requires: Pygments-python3 = %{version}-%{release}
Requires: pyflakes
Requires: pylint
Requires: tox
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-qmake
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes
BuildRequires : pylint
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Pygments
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
%setup -q -n Pygments-2.7.1
cd %{_builddir}/Pygments-2.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600912072
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
cp %{_builddir}/Pygments-2.7.1/LICENSE %{buildroot}/usr/share/package-licenses/Pygments/68f012ad90d61adc14c6ea68f3480e358cf46cbe
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
/usr/share/package-licenses/Pygments/68f012ad90d61adc14c6ea68f3480e358cf46cbe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
