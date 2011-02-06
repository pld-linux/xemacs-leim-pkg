Summary:	Quail - all non-English and non-Japanese language support
Summary(pl.UTF-8):	Quail - obsługa wszystkich języków innych niż angielski i japoński
Name:		xemacs-leim-pkg
%define 	srcname	leim
Version:	1.22
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	942fbcd4d56eb59529bbd15c3b6c0b3b
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-mule-base-pkg
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quail - all non-English and non-Japanese language support.

%description -l pl.UTF-8
Quail - obsługa wszystkich języków innych niż angielski i japoński.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/leim/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/leim
%{_datadir}/xemacs-packages/lisp/leim/*.elc
%dir %{_datadir}/xemacs-packages/lisp/leim/quail
%{_datadir}/xemacs-packages/lisp/leim/quail/*.elc
