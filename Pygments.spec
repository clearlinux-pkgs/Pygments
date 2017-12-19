#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0A5B101836580288 (georg@python.org)
#
Name     : Pygments
Version  : 2.2.0
Release  : 31
URL      : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz
Source0  : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz
Source99 : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz.asc
Summary  : Pygments is a syntax highlighting package written in Python.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Pygments-bin
Requires: Pygments-legacypython
Requires: Pygments-python3
Requires: Pygments-python
BuildRequires : go
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
~~~~~~~~
        
            Pygments is a syntax highlighting package written in Python.
        
            It is a generic syntax highlighter suitable for use in code hosting, forums,
            wikis or other applications that need to prettify source code.  Highlights

%package bin
Summary: bin components for the Pygments package.
Group: Binaries

%description bin
bin components for the Pygments package.


%package legacypython
Summary: legacypython components for the Pygments package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Pygments package.


%package python
Summary: python components for the Pygments package.
Group: Default
Requires: Pygments-legacypython
Requires: Pygments-python3
Provides: pygments-python

%description python
python components for the Pygments package.


%package python3
Summary: python3 components for the Pygments package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Pygments package.


%prep
%setup -q -n Pygments-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169217
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507169217
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pygmentize

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
