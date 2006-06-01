%define	min_jre	1.4
Summary:	jEdit - cross platform programmer's text editor
Summary(pl):	jEdit - miêdzyplatformowy tekstowy edytor programisty
Name:		jedit
Version:	4.3
%define _pre	pre4
Release:	0.%{_pre}.1
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/jedit/%{name}%{version}%{_pre}source.tar.gz
# Source0-md5:	0e33e86a97e2426818798b5f1ac56485
Source1:	%{name}.desktop
URL:		http://www.jedit.org/
BuildRequires:	docbook-style-xsl
BuildRequires:	ant
BuildRequires:	jdk >= %{min_jre}
BuildRequires:	libxslt-progs
BuildRequires:	xml-commons
Requires:	jre >= %{min_jre}
Requires:	jre-X11 >= %{min_jre}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jEdit is a cross platform programmer's text editor written in Java.

%description -l pl
jEdit to miêdzyplatformowy tekstowy edytor programisty napisany w
Javie.

%prep
%setup -q -n jEdit

%build
JAVA_HOME="%{java_home}"; export JAVA_HOME
echo 'docbook.xsl=/usr/share/sgml/docbook/xsl-stylesheets' > build.properties

# use xsltproc to build docs (it works, xalan doesn't)
ant dist docs-html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/jedit/doc/{FAQ,users-guide},%{_bindir}}

install jedit.jar $RPM_BUILD_ROOT%{_datadir}/jedit
cp -rf modes macros $RPM_BUILD_ROOT%{_datadir}/jedit

# used as online documentation
install doc/*.{txt,png,html} $RPM_BUILD_ROOT%{_datadir}/jedit/doc
install doc/FAQ/*.* $RPM_BUILD_ROOT%{_datadir}/jedit/doc/FAQ
cp -a doc/tips $RPM_BUILD_ROOT%{_datadir}/jedit/doc
cp -a doc/news42 $RPM_BUILD_ROOT%{_datadir}/jedit/doc
install doc/users-guide/*.* $RPM_BUILD_ROOT%{_datadir}/jedit/doc/users-guide
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D doc/jedit.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

cat > $RPM_BUILD_ROOT%{_bindir}/jedit <<EOF
#!/bin/sh
java -jar %{_datadir}/jedit/jedit.jar
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# already present as online docs
#%doc doc/{CHANGES.txt,README.txt,TODO.txt}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jedit
%{_desktopdir}/*
%{_pixmapsdir}/*.png
