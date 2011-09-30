%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname arel
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Arel is a Relational Algebra for Ruby
Name: rubygem-%{gemname}
Version: 2.0.9
Release: %mkrel 1
Group: Development/Ruby 
License: MIT
URL: http://github.com/rails/%{gemname}

Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
# Fix for test failure. This fix is relevant only for 2.0.x release.
# https://github.com/rails/arel/commit/a1662156b3abb8830f7245bd6e398cf2ca1291d4
Patch0: disable-failing-test.patch

Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygem(minitest)
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


%package doc
Summary: Documentation for %{name}
Group: Development/Ruby 
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force --rdoc %{SOURCE0}

pushd .%{geminstdir}
%patch0

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

rm %{buildroot}/%{geminstdir}/.autotest
rm %{buildroot}/%{geminstdir}/.gemtest

%check
pushd %{buildroot}/%{geminstdir}/test
ruby -I../lib -e "Dir.glob('**/test_*').each {|t| require t}"
popd

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/MIT-LICENSE.txt
%doc %{geminstdir}/README.markdown
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%{geminstdir}/test
%{geminstdir}/arel.gemspec
%doc %{geminstdir}/Manifest.txt
%{geminstdir}/Rakefile
%doc %{gemdir}/doc/%{gemname}-%{version}
