#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Template
%define		pnam	Plugin-Stash
Summary:	Template::Plugin::Stash - expose the stash, ideal for Dumpering
Summary(pl.UTF-8):	Template::Plugin::Stash - wystawianie schowka, idealne do zrzucania
Name:		perl-Template-Plugin-Stash
Version:	1.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c640985f5b36a30a5af4cd5ab455b97
URL:		http://search.cpan.org/dist/Template-Plugin-Stash/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template::Plugin::Stash - expose the stash, ideal for Dumpering...

%description -l pl.UTF-8
Template::Plugin::Stash - wystawianie schowka, idealne do zrzucania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Template/Plugin/Stash.pm
%{_mandir}/man3/*
