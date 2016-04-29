#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-code_statistics
Version  : 0.2.13
Release  : 8
URL      : https://rubygems.org/downloads/code_statistics-0.2.13.gem
Source0  : https://rubygems.org/downloads/code_statistics-0.2.13.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-code_statistics-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-construct
BuildRequires : rubygem-test-unit
BuildRequires : rubygem-thoughtbot-shoulda

%description
= code_statistics
This is a port of the rails 'rake stat' so it can be used on none rails projects and have it's features slowly expanded. Please feel free to contact us if you have any ideas for additional stats that should be added. It in general tries to have defaults that work better for both rails and non rails projects. It specifically supports cucumber tests and rspec better than the original rails stats.

%package bin
Summary: bin components for the rubygem-code_statistics package.
Group: Binaries

%description bin
bin components for the rubygem-code_statistics package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n code_statistics-0.2.13
gem spec %{SOURCE0} -l --ruby > rubygem-code_statistics.gemspec

%build
gem build rubygem-code_statistics.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
code_statistics-0.2.13.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/code_statistics-0.2.13
ruby -v -I.:lib:test test*/test_*.rb
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/code_statistics-0.2.13.gem
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/.document
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/bin/code_statistics
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/code_statistics.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/lib/code_statistics.rb
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/lib/code_statistics/code_statistics.rb
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/lib/tasks/code_stats.rb
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/test/code_statistics_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/code_statistics-0.2.13/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/code_statistics-0.2.13.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/code_statistics
