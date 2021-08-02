# Conditional build:
%bcond_without	tests	# unit tests
%define		module	doxyqml
Summary:	Doxyqml
Summary(pl.UTF-8):	Doxyqml
Name:		python3-%{module}
Version:	0.5.1
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://invent.kde.org/sdk/doxyqml/-/archive/%{version}/%{module}-%{version}.tar.bz2
# Source0-md5:	7935ea56fc6ce9a102737fd93cf493a9
URL:		https://agateau.com/projects/doxyqml/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doxyqml lets you use Doxygen to document your QML classes.

%description -l pl.UTF-8
Doxyqml pozwala Ci użycić Doxygena do dokumentowania Twoich
klas QML.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/%{module}
%attr(755,root,root) %{_bindir}/doxyqml
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
