#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.deprecation
Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Name:		python-%{module}
Version:	4.0.2
Release:	3
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.deprecation/zope.deprecation-%{version}.tar.gz
# Source0-md5:	5f8cecce85f2783f9e020f1288e908fd
URL:		http://docs.zope.org/zope.deprecation/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-setuptools
%endif
Requires:	python-zope.testing
Obsoletes:	Zope-Deprecation
Provides:	Zope-Deprecation
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple function called deprecated(names, reason) to
mark deprecated modules, classes, functions, methods and properties.

%description -l pl.UTF-8
Biblioteka odradzająca dla kodu w Pythonie.

%package -n python3-%{module}
Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Group:		Libraries/Python
Requires:	python3-zope.testing

%description -n python3-%{module}
This package provides a simple function called deprecated(names, reason) to
mark deprecated modules, classes, functions, methods and properties.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka odradzająca dla kodu w Pythonie.

%prep
%setup -q -n zope.deprecation-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
# py_sitedir needed as there is the rest of zope.* and it contains some platform-specific code
%py_install \
	--install-purelib=%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
# py_sitedir needed as there is the rest of zope.* and it contains some platform-specific code
%py3_install \
	--install-purelib=%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py_sitedir}/zope/deprecation
%{py_sitedir}/zope/deprecation/*.py[co]
%{py_sitedir}/zope.deprecation-*.egg-info
%{py_sitedir}/zope.deprecation-*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt
%{py3_sitedir}/zope/deprecation
%{py3_sitedir}/zope.deprecation-*.egg-info
%{py3_sitedir}/zope.deprecation-*-nspkg.pth
%endif
