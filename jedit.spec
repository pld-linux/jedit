Summary:	jEdit - cross platform programmer's text editor
Summary(pl):	jEdit - mi�dzyplatformowy tekstowy edytor programisty
Name:		jedit
Version:	4.2
Release:	1
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/jedit/%{name}%(echo %{version} | tr -d .)source.tar.gz
# Source0-md5:	c7fa902fd5ad3207efb45c9171eaacf1
Source1:	%{name}.desktop
URL:		http://www.jedit.org/
BuildRequires:	docbook-style-xsl
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.3
BuildRequires:	libxslt-progs
Requires:	jre >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jEdit is a cross platform programmer's text editor written in Java.

%description -l pl
jEdit to mi�dzyplatformowy tekstowy edytor programisty napisany w
Javie.

%prep
%setup -q -n jEdit

%build
JAVA_HOME=%{_libdir}/java; export JAVA_HOME
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
cp -rf doc/tips $RPM_BUILD_ROOT%{_datadir}/jedit/doc
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
