%define rubyver		1.9.2
%define rubyminorver	p0

Name:		ruby19
Version:	%{rubyver}%{rubyminorver}
Release:	3%{?dist}
License:	Ruby License/GPL - see COPYING
URL:		http://www.ruby-lang.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc
Source0:	ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:	An interpreter of object-oriented scripting language
Group:		Development/Languages

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}
%build
CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export CFLAGS
%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --program-suffix=19

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/lib/
rm -rf $RPM_BUILD_ROOT/usr/share/doc/ruby
rm -rf $RPM_BUILD_ROOT/usr/src
rm -f $RPM_BUILD_ROOT/usr/lib64/libruby-static.a
rm -f $RPM_BUILD_ROOT/usr/lib64/libruby.so


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc README COPYING ChangeLog LEGAL ToDo 
%{_bindir}
%{_includedir}
%{_prefix}/lib64/
%{_prefix}/share/

%changelog
* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p0-3
- Disable X11 support
- Disable tk support

* Fri Dec 17 2010 Sergio Rubio <rubiojr@frameos.org> - 1.9.2p0-2
- renamed package to ruby19
- ruby bin renamed to ruby19
- install using standard prefix

* Fri Nov 15 2010 Taylor Kimball <taylor@linuxhq.org> - 1.9.2-p0-1
- Initial build for el5 based off of el5 spec.
