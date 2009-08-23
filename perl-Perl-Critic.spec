%define upstream_name       Perl-Critic
%define upstream_version    1.103

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Critique Perl source for style and standards
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz
Requires:       perl(Module::Pluggable)
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
%setup -q -n %{upstream_name}-%{upstream_version} 

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


