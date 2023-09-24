#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.deprecation
Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Name:		python-%{module}
# keep 4.x here for python2 support
Version:	4.4.0
Release:	3
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.deprecation/zope.deprecation-%{version}.tar.gz
# Source0-md5:	6915a92473e2658b3954f8490938455c
URL:		https://www.zope.dev/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-zope.testrunner
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testrunner
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
Provides:	Zope-Deprecation
Obsoletes:	Zope-Deprecation < 4.1.0
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

%package -n python3-%{module}
Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This package provides a simple function called deprecated(names,
reason) to mark deprecated modules, classes, functions, methods and
properties.

%description -n python3-%{module} -l pl.UTF-8
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
%setup -q -n zope.deprecation-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py_sitescriptdir}/zope/deprecation
%{py_sitescriptdir}/zope.deprecation-*.egg-info
%{py_sitescriptdir}/zope.deprecation-*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/deprecation
%{py3_sitescriptdir}/zope.deprecation-*.egg-info
%{py3_sitescriptdir}/zope.deprecation-*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
