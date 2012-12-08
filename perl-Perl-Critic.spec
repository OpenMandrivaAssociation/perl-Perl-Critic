%define upstream_name       Perl-Critic
%define upstream_version 1.116

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Critique Perl source for style and standards
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Keywords)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Exception::Class)
BuildRequires:  perl(IO::String)
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
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Perl
%{perl_vendorlib}/Test
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.116.0-4mdv2012.0
+ Revision: 765591
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.116.0-2
+ Revision: 676636
- rebuild

* Mon May 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.116.0-1
+ Revision: 675018
- update to new version 1.116

* Fri May 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.115.0-1
+ Revision: 669912
- new version
- update to new version 1.111

* Thu Sep 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.109.0-1mdv2011.0
+ Revision: 575401
- update to 1.109

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.108.0-1mdv2011.0
+ Revision: 553045
- adding missing buildrequires:
- update to 1.108

* Wed Sep 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.105.0-1mdv2010.0
+ Revision: 434674
- new version

* Mon Aug 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.104.0-1mdv2010.0
+ Revision: 420280
- update to new version 1.104

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.103.0-1mdv2010.0
+ Revision: 419923
- update to new version 1.103

* Sun Jul 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 397434
- new version
- use %%perl_convert_version macro

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.098-1mdv2009.1
+ Revision: 352916
- update to new version 1.098

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.096-1mdv2009.1
+ Revision: 336811
- update to new version 1.096

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.092-1mdv2009.0
+ Revision: 281116
- update to new version 1.092

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.090-1mdv2009.0
+ Revision: 242074
- update to new version 1.090

* Sat Jul 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.088-1mdv2009.0
+ Revision: 232000
- update to new version 1.088

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.087-1mdv2009.0
+ Revision: 227974
- update to new version 1.087

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.086-1mdv2009.0
+ Revision: 218744
- update to new version 1.086

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.085-1mdv2009.0
+ Revision: 217101
- update to new version 1.085

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.084-1mdv2009.0
+ Revision: 212226
- update to new version 1.084

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.082-1mdv2008.1
+ Revision: 183106
- update to new version 1.082

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.080-1mdv2008.1
+ Revision: 109520
- update to new version 1.080

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.078-1mdv2008.1
+ Revision: 97559
- update to new version 1.078

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.074-1mdv2008.0
+ Revision: 81160
- update to new version 1.074

* Wed Sep 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.073-1mdv2008.0
+ Revision: 79774
- update to new version 1.073

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.071-1mdv2008.0
+ Revision: 75282
- update to new version 1.071

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.061-1mdv2008.0
+ Revision: 55821
- update to new version 1.061

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2008.0
+ Revision: 47720
- update to new version 1.06


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2007.0
+ Revision: 120839
- new version

* Tue Feb 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2007.1
+ Revision: 120321
- new version

* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2007.1
+ Revision: 100257
- new version

* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2007.1
+ Revision: 84621
- new version
- Import perl-Perl-Critic

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2007.0
- New version 0.19
- higher version needed for PPI

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-2mdv2007.0
- requires perl(Module::Pluggable)

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2007.0
- New version 0.18

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2007.0
- New version 0.17

* Wed May 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdk
- New release 0.16

* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-2mdk
- better buildrequires syntax
- better source URL
- buildrequires fix

* Thu Mar 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdk
- New release 0.15

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-2mdk
- fix buildrequires

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- New release 0.14

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.13-3mdk
- Add BuildRequires perl-IO-String

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-2mdk
- buildrequires perl-Config-Tiny

* Thu Nov 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- first mdk release

