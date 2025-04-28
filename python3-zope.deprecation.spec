#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define	module	zope.deprecation
Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Name:		python3-%{module}
Version:	5.1
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.deprecation/zope_deprecation-%{version}.tar.gz
# Source0-md5:	a971b204cf636bf65ba8418a317b3245
URL:		https://www.zope.dev/
BuildRequires:	python3 >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple function called deprecated(names,
reason) to mark deprecated modules, classes, functions, methods and
properties.

%description -l pl.UTF-8
Ten pakiet udostępnia prostą funkcję o nazwie deprecated(names,
reason), służącą do oznaczania przestarzałych modułów, klas, funkcji,
metod i własności.

%package apidocs
Summary:	API documentation for Python zope.deprecation module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.deprecation
Group:		Documentation

%description apidocs
API documentation for Python zope.deprecation module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.deprecation.

%prep
%setup -q -n zope_deprecation-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
zope-testrunner-3 --test-path=src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/deprecation
%{py3_sitescriptdir}/zope.deprecation-*.egg-info
%{py3_sitescriptdir}/zope.deprecation-*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
