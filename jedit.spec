Summary:	jEdit - cross platform programmer's text editor
Summary(pl):	jEdit - miêdzyplatformowy tekstowy edytor programisty
Name:		jedit
Version:	4.1pre4
Release:	1
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/jedit/%{name}%(echo %{version} | tr -d .)source.tar.gz
# Source0-md5:	0f1ecb731411ee738a29d46d09036cc2
URL:		http://www.jedit.org/
BuildRequires:	docbook-style-xsl = 1.53.0
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.3
BuildRequires:	libxslt-progs
Requires:	jre >= 1.3
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
JAVA_HOME="/usr/lib/java"; export JAVA_HOME
echo 'docbook.xsl=/usr/share/sgml/docbook/xsl-stylesheets-1.53.0' > build.properties

# use xsltproc to build docs (it works, xalan doesn't)
ant dist docs-html-xsltproc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/jedit/doc/{FAQ,users-guide},%{_bindir}}

install jedit.jar $RPM_BUILD_ROOT%{_datadir}/jedit
cp -rf modes macros $RPM_BUILD_ROOT%{_datadir}/jedit

# used as online documentation
install doc/*.{txt,png,html} $RPM_BUILD_ROOT%{_datadir}/jedit/doc
install doc/FAQ/*.html $RPM_BUILD_ROOT%{_datadir}/jedit/doc/FAQ
cp -rf doc/tips $RPM_BUILD_ROOT%{_datadir}/jedit/doc
install doc/users-guide/*.html $RPM_BUILD_ROOT%{_datadir}/jedit/doc/users-guide

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
