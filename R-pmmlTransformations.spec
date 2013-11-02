%global packname  pmmlTransformations
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2.1
Release:          1
Summary:          Transforms input data from a PMML perspective
Group:            Sciences/Mathematics
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core



Requires:         R-pmml 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

BuildRequires:   R-pmml 
%description
Allows for data to be transformed before using it to construct models.
Builds structures to allow functions in the PMML package to output
transformation details in addition to the model in the resulting PMML

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
