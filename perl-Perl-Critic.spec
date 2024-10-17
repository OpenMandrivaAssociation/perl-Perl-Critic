%define modname	Perl-Critic
%define modver 1.123

Summary:	Critique Perl source for style and standards
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(B::Keywords)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl(Pod::Spell)
BuildRequires:	perl(PPI) >= 1.118.0
BuildRequires:	perl(PPIx::Utilities::Statement)
BuildRequires:	perl(PPIx::Regexp)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Set::Scalar)
BuildRequires:	perl(String::Format)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl-devel
Requires:	perl(Module::Pluggable)

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
%setup -qn %{modname}-%{modver} 

%build
%__perl Build.PL --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Perl
%{perl_vendorlib}/Test
%{_mandir}/man1/*
%{_mandir}/man3/*



