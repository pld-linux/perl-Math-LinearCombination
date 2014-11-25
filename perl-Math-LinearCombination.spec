#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	LinearCombination
%include	/usr/lib/rpm/macros.perl
Summary:	Math::LinearCombination - sum of variables with a numerical coefficient
Summary(pl.UTF-8):	Math::LinearCombination - suma zmiennych ze współczynnikami liczbowymi
Name:		perl-Math-LinearCombination
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a8b0e49dda41f288cbb8f1d384209f9
URL:		http://search.cpan.org/dist/Math-LinearCombination/
BuildRequires:	perl-Math-SimpleVariable >= 0.03
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Math::LinearCombination to moduł służący do reprezentowania
matematycznych kombinacji liniowych zmiennych, czyli wyrażeń w postaci

  a1 * x1 + a2 * x2 + ... + an * xn

gdzie x1, x2, ... xn to zmienne, a a1, a2, ... an to liczbowe
współczynniki. Obsługiwane jest także obliczanie wartości i
manipulowanie kombinacjami liniowymi. Współczynniki liczbowe a_i oraz
zmienne x_i są zapisywane jako pary w wewnętrznej strukturze danych i
nie powinny być modyfikowane ani odczytywane bezpośrednio, lecz przez
udostępnione metody.

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
