%define upstream_name	 Image-Base
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Base class for loading, manipulating and saving images
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This class should not be used directly. Known inheritors are Image::Xbm and
Image::Xpm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.160.0-1mdv2011
+ Revision: 690267
- update to new version 1.16

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.150.0-2
+ Revision: 640768
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.150.0-1
+ Revision: 638911
- update to new version 1.15

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.140.0-1
+ Revision: 634271
- update to new version 1.14

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 601876
- update to new version 1.12
- update to new version 1.11

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 402540
- update to 0.56

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.07-11mdv2009.0
+ Revision: 241485
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-9mdv2008.0
+ Revision: 86475
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-8mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-7mdk
- better summary and description
- spec cleanup
- better URL
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-6mdk 
- remove MANIFEST

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-5mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-4mdk 
- fix directory ownership (distlint)
- make test

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-3mdk 
- rpmbuildupdate aware

