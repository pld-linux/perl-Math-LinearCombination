#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	LinearCombination
Summary:	Math::LinearCombination - sum of variables with a numerical coefficient
Summary(pl):	Math::LinearCombination - suma zmiennych ze wspó³czynnikami liczbowymi
Name:		perl-Math-LinearCombination
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a8b0e49dda41f288cbb8f1d384209f9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Math-SimpleVariable >= 0.03
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-SimpleVariable >= 0.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::LinearCombination is a module for representing mathematical
linear combinations of variables, i.e. expressions of the format

  a1 * x1 + a2 * x2 + ... + an * xn

with x1, x2, ..., xn variables, and a1, a2, ..., an numerical
coefficients. Evaluation and manipulation of linear combinations is
also supported. The numerical coefficients a_i and variables x_i are
stored as pairs in an internal data structure and should not be
manipulated directly. All access and manipulation should be performed
through the methods.

%description -l pl
Math::LinearCombination to modu³ s³u¿±cy do reprezentowania
matematycznych kombinacji liniowych zmiennych, czyli wyra¿eñ w postaci

  a1 * x1 + a2 * x2 + ... + an * xn

gdzie x1, x2, ... xn to zmienne, a a1, a2, ... an to liczbowe
wspó³czynniki. Obs³ugiwane jest tak¿e obliczanie warto¶ci i
manipulowanie kombinacjami liniowymi. Wspó³czynniki liczbowe a_i oraz
zmienne x_i s± zapisywane jako pary w wewnêtrznej strukturze danych i
nie powinny byæ modyfikowane ani odczytywane bezpo¶rednio, lecz przez
udostêpnione metody.

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
%{perl_vendorlib}/Math/LinearCombination.pm
%{_mandir}/man3/*
