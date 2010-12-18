%define upstream_name       Perl-Critic
%define upstream_version 1.111

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Critique Perl source for style and standards
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Keywords)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Exception::Class)
BuildRequires:  perl(IO::String)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl(PPI) >= 1.118.0
BuildRequires:	perl(PPIx::Utilities::Statement)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Set::Scalar)
BuildRequires:	perl(String::Format)
BuildRequires:	perl(Task::Weaken)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:       perl(Module::Pluggable)

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
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Perl
%{perl_vendorlib}/Test
%{_bindir}/*
%{_mandir}/*/*
