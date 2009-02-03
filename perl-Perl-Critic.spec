%define	module	Perl-Critic
%define	name	perl-%{module}
%define version 1.096
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Critique Perl source for style and standards
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Perl/%{module}-%{version}.tar.bz2
Requires:       perl(Module::Pluggable)
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(PPI) >= 1.118
BuildRequires:	perl(String::Format)
BuildRequires:	perl(Config::Tiny)
BuildRequires:  perl(IO::String)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl(Set::Scalar)
BuildRequires:	perl(B::Keywords)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Exception::Class)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code analysis
engine. Perl::Critic is distributed with a number of Perl::Critic::Policy
modules that attempt to enforce various coding guidelines. Most Policies are
based on Damian Conway's book Perl Best Practices. You can choose and customize
those Polices through the Perl::Critic interface. You can also create new
Policy modules that suit your own tastes.

For a convenient command-line interface to Perl::Critic, see the documentation
for perlcritic. If you want to integrate Perl::Critic with your build process,
Test::Perl::Critic provides a nice interface that is suitable for test scripts.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Perl
%{_bindir}/*
%{_mandir}/*/*


