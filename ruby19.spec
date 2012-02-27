%define rubyver		1.9.2
%define rubyminorver	p290

Name:		ruby19
Version:	%{rubyver}%{rubyminorver}
Release:	3%{?dist}
License:	Ruby License/GPL - see COPYING
URL:		http://www.ruby-lang.org/
Provides:       ruby(abi) = 1.9
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc /bin/sed
Source0:	ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Patch0:         ruby-mkmf_static.patch
Summary:	An interpreter of object-oriented scripting language
Group:		Development/Languages

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export CFLAGS
%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --program-suffix=19

export LD_LIBRARY_PATH=$(pwd)
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libruby-static.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libruby.so
# Fix libruby linking
sed -i 's/\(.*LIBRUBYARG_SHARED.*=\).*/\1 "$(libdir)\/lib$(RUBY_SO_NAME).so.$(ruby_version)"/' $RPM_BUILD_ROOT%{_libdir}/ruby/1.9.1/%{_arch}-%{_os}/rbconfig.rb

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc README COPYING ChangeLog LEGAL ToDo 
%{_bindir}
%{_includedir}
%{_libdir}
%{_prefix}/share/

%changelog
* Mon Feb 27 2012 Mihael Leinartas <mleinartas@gmail.com> - 1.9.2p290-3
- Fix mkmf.rb using libruby-static for lib detection

* Sat Jan 28 2012 Michael Leinartas <mleinartas@gmail.com> - 1.9.2p290-2
- Fix linking of compiled gem extensions

* Fri Jul 22 2011 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p290-1
- ruby19.spec

* Fri May 06 2011 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p180-3
- fixed i386 build

* Thu May 05 2011 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p180-2
- fix i386 build

* Fri Feb 18 2011 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p180-1
- updated to 1.9.2p180

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p0-3
- Disable X11 support
- Disable tk support

* Fri Dec 17 2010 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p0-2
- renamed package to ruby19
- ruby bin renamed to ruby19
- install using standard prefix

* Fri Nov 15 2010 Taylor Kimball <taylor@linuxhq.org> - 1.9.2-p0-1
- Initial build for el5 based off of el5 spec.
