# Generated from arel-3.0.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	arel

Summary:	Arel is a SQL AST manager for Ruby
Name:		rubygem-%{rbname}

Version:	3.0.2
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/rails/arel
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
# required by check suite
BuildRequires:	rubygem(hoe)
BuildArch:	noarch

%description
Arel is a SQL AST manager for Ruby. It
1. Simplifies the generation of complex SQL queries
2. Adapts to various RDBMS systems
It is intended to be a framework framework; that is, you can build your own
ORM
with it, focusing on innovative object and collection modeling as opposed to
database compatibility and query generation.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%check
rake test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt


%changelog
* Thu Apr 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.2-1
+ Revision: 789358
- version update 3.0.2

* Thu Feb 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.0.0-1
+ Revision: 775076
- add rubygem(hoe) to buildrequires for check suite
- regenerate spec with gem2rpm5
- new version
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Sep 30 2011 Alexander Barakin <abarakin@mandriva.org> 2.0.9-1
+ Revision: 702146
- missing rdoc fix
- imported package rubygem-arel

