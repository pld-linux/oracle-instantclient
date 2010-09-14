#
# Conditional build:
%bcond_with	lite		# build basic lite version of client

%define		x86ver		11.2.0.1
%define		x8664ver	11.2.0.1.0-1

Summary:	Oracle Database Instant Client
Name:		oracle-instantclient
Version:	11.2.0.1.0
Release:	2
License:	OTN (proprietary, non-distributable)
Group:		Applications/Databases
Source0:	instantclient-basic-linux32-%{x86ver}.zip
# NoSource0-md5:	5d8bba5d245b885dc8a6fda5ec6e6442
Source1:	instantclient-basiclite-linux32-%{x86ver}.zip
# NoSource1-md5:	ae2966345030aa2d78fe3d143c8d83ff
Source2:	instantclient-sdk-linux32-%{x86ver}.zip
# NoSource2-md5:	374e1986621cb83ec90d4714c5430473
Source3:	instantclient-jdbc-linux32-%{x86ver}.zip
# NoSource3-md5:	e4ef505b542eb4dec665d659a6830e9d
Source4:	instantclient-odbc-linux32-%{x86ver}.zip
# NoSource4-md5:	55a09a9ba803dbc3f9d053a9cba8af2d
Source5:	instantclient-sqlplus-linux32-%{x86ver}.zip
# NoSource5-md5:	94a004ee4f58149e62ed76107217d7c8
Source6:	instantclient-tools-linux32-%{x86ver}.zip
# NoSource6-md5:	b63f8b6b44029775eb1a34b1d8e3d24c
Source10:	oracle-instantclient11.2-basic-%{x8664ver}.x86_64.zip
# NoSource10-md5:	7d96ba339c3cb6d5ba5f2b40ed7ed02d
Source11:	oracle-instantclient11.2-basiclite-%{x8664ver}.x86_64.zip
# NoSource11-md5:	885664cec6413c2c7e7e7928b76e7478
Source12:	oracle-instantclient11.2-sdk-%{x8664ver}.x86_64.zip
# NoSource12-md5:	ee46ae0ec92397cb9b0cef4f48e0eda7
Source13:	oracle-instantclient11.2-jdbc-%{x8664ver}.x86_64.zip
# NoSource13-md5:	5bb71717e0ff6f9e98eb874b1d72abe1
Source14:	oracle-instantclient11.2-odbc-%{x8664ver}.x86_64.zip
# NoSource14-md5:	5bb55794190d4131133c92adfba57f8a
Source15:	oracle-instantclient11.2-sqlplus-%{x8664ver}.x86_64.zip
# NoSource15-md5:	1fdc0c3544194de35d2aabe9e6b3faf5
Source16:	oracle-instantclient11.2-tools-%{x8664ver}.x86_64.zip
# NoSource16-md5:	a9d95d2500ec932837abf92802a2409f
# http://duberga.net/dbd_oracle_instantclient_linux/oracle-instantclient-config
Source20:	oracle-instantclient-config.in
Source21:	oracle-instantclient.pc.in
NoSource:	0
NoSource:	1
NoSource:	2
NoSource:	3
NoSource:	4
NoSource:	5
NoSource:	6
NoSource:	10
NoSource:	11
NoSource:	12
NoSource:	13
NoSource:	14
NoSource:	15
NoSource:	16
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
BuildRequires:	sed
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orcale Database Instant Client Package.

%package basic
Summary:	Oracle Database Instant Client - Basic
Group:		Applications/Databases
Provides:	%{name} = %{version}-%{release}

%description basic
Orcale Database Instant Client Package - Basic.
All files required to run OCI, and OCCI, and JDBC-OCI applications.

%package basiclite
Summary:	Oracle Database Instant Client - Basic Lite
Group:		Applications/Databases
Provides:	%{name} = %{version}-%{release}

%description basiclite
Orcale Database Instant Client Package - Basic Lite.
All files required to run OCI, and OCCI, and JDBC-OCI applications.

This package contains only English error messages and Unicode, ASCII,
and Western European character set suppor

%package devel
Summary:	SDK for Oracle Database Instant Client
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Oracle Database Instant Client Package - SDK.
Additional header files and an example makefile for developing
Oracle applications with Instant Client.

%package jdbc
Summary:	JDBC for Oracle Database Instant Client
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}

%description jdbc
Oracle Database Instant Client Package - JDBC.
Support for JDBC-OCI, XA, Internationalization, and RowSet
operations under JDBC.

%package jdbc-devel
Summary:	JDBC for Oracle Database Instant Client development files
Group:		Development/Languages/Java
Requires:	%{name}-jdbc = %{version}-%{release}

%description jdbc-devel
Oracle Database Instant Client Package - JDBC development files.

%package odbc
Summary:	ODBC for Oracle Database Instant Client
Group:		Libraries
Requires(post,preun):	/usr/bin/odbcinst
Requires:	%{name} = %{version}-%{release}
Requires:	unixODBC

%description odbc
Oracle Database Instant Client Package - ODBC.
Additional libraries for enabling ODBC applications.

%package sqlplus
Summary:	Oracle Database Client - SQL*Plus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description sqlplus
Oracle Database Instant Client Package - SQL*Plus.
Additional libraries and executable for running SQL*Plus
with Instant Client.

%package tools
Summary:	Oracle Database Workload Replay Client
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description tools
Oracle Database Instant Client Package - WRC.
Workload Replay Client used to replay workload
for RAT's DB Replay Feature.

%prep
%ifarch %{ix86}
%setup -q -c -T -b %{?with_lite:1}%{!?with_lite:0} -b 2 -b 3 -b 4 -b 5 -b 6
%endif

%ifarch %{x8664}
%setup -q -c -T -b %{?with_lite:11}%{!?with_lite:10} -b 12 -b 13 -b 14 -b 15 -b 16
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus/admin} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_includedir}/oracle/client} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_javadir}}

cd instantclient_*

install -p *.jar $RPM_BUILD_ROOT%{_javadir}
install -p *.so* $RPM_BUILD_ROOT%{_libdir}
install -p sqlplus $RPM_BUILD_ROOT%{_bindir}
install -p genezi $RPM_BUILD_ROOT%{_bindir}
install -p adrci $RPM_BUILD_ROOT%{_bindir}
install -p wrc $RPM_BUILD_ROOT%{_bindir}
install -p glogin.sql $RPM_BUILD_ROOT%{_datadir}/sqlplus/admin

%{__sed} -e 's|@@prefix@@|%{_prefix}|' \
	-e 's|@@libdir@@|%{_libdir}|' \
	-e 's|@@includedir@@|%{_includedir}/oracle/client|' \
	-e 's|@@version@@|%{version}|' %{SOURCE20} > \
		$RPM_BUILD_ROOT%{_bindir}/oracle-instantclient-config

%{__sed} -e 's|@@prefix@@|%{_prefix}|' \
	-e 's|@@libdir@@|%{_libdir}|' \
	-e 's|@@includedir@@|%{_includedir}/oracle/client|' \
	-e 's|@@version@@|%{version}|' %{SOURCE21} > \
		$RPM_BUILD_ROOT%{_pkgconfigdir}/oracle-instantclient.pc

install -p sdk/ottclasses.zip $RPM_BUILD_ROOT%{_javadir}
install -p sdk/ott $RPM_BUILD_ROOT%{_bindir}
install -p sdk/include/* $RPM_BUILD_ROOT%{_includedir}/oracle/client
install -p sdk/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

cat <<EOF >/etc/tnsnames.ora
ORCL =
  (DESCRIPTION =
      (ADDRESS_LIST =
        (ADDRESS =
	  (PROTOCOL = TCP)
	  (Host = localhost)
	  (Port = 1521)
	)
      )
      (CONNECT_DATA = (SID = ORCL)
      )
  )
EOF

# rename to avoid clash with openldap header or php build will suffer
mv $RPM_BUILD_ROOT%{_includedir}/oracle/client/{ldap.h,oraldap.h}

cd $RPM_BUILD_ROOT%{_libdir}
for ff in lib*.so.* ; do
	ln -s $ff ${ff:%%.so.*}.so
done

%clean
rm -rf $RPM_BUILD_ROOT

%post basic -p /sbin/ldconfig
%postun basic -p /sbin/ldconfig

%post basiclite -p /sbin/ldconfig
%postun basiclite -p /sbin/ldconfig

%post jdbc -p /sbin/ldconfig
%postun jdbc -p /sbin/ldconfig

%post sqlplus -p /sbin/ldconfig
%postun sqlplus -p /sbin/ldconfig

%post odbc
/sbin/ldconfig
# install Orcale driver
/usr/bin/odbcinst -i -d -r <<EOF
[Oracle 11g]
Description = Oracle ODBC driver for Oracle 11g
Driver = %{_libdir}/libsqora.so.11.1
Setup = 
EOF

%preun odbc
/usr/bin/odbcinst -u -d -n "Oracle 11g" || true

%postun odbc -p /sbin/ldconfig

%if %{with lite}
%files basiclite
%defattr(644,root,root,755)
%doc instantclient_*/BASIC_LITE_README
%config(noreplace) %verify(not md5 mtime size) /etc/tnsnames.ora
%attr(755,root,root) %{_bindir}/adrci
%attr(755,root,root) %{_bindir}/genezi
%attr(755,root,root) %{_libdir}/libclntsh.so.*
%attr(755,root,root) %{_libdir}/libocci.so.*
%attr(755,root,root) %{_libdir}/libociicus.so
%attr(755,root,root) %{_libdir}/libnnz11.so
%attr(755,root,root) %{_libdir}/libocijdbc11.so
%else
%files basic
%defattr(644,root,root,755)
%doc instantclient_*/BASIC_README
%config(noreplace) %verify(not md5 mtime size) /etc/tnsnames.ora
%attr(755,root,root) %{_bindir}/adrci
%attr(755,root,root) %{_bindir}/genezi
%attr(755,root,root) %{_libdir}/libclntsh.so.*
%attr(755,root,root) %{_libdir}/libocci.so.*
%attr(755,root,root) %{_libdir}/libnnz11.so
%attr(755,root,root) %{_libdir}/libociei.so
%attr(755,root,root) %{_libdir}/libocijdbc11.so
%endif

%files devel
%defattr(644,root,root,755)
%doc instantclient_*/sdk/SDK_README
%attr(755,root,root) %{_bindir}/oracle-instantclient-config
%attr(755,root,root) %{_bindir}/ott
%attr(755,root,root) %{_libdir}/libclntsh.so
%attr(755,root,root) %{_libdir}/libocci.so
%{_pkgconfigdir}/oracle-instantclient.pc
%{_includedir}/oracle/client
%{_javadir}/*.zip
%{_examplesdir}/%{name}

%files jdbc
%defattr(644,root,root,755)
%doc instantclient_*/JDBC_README
%attr(755,root,root) %{_libdir}/libheteroxa11.so
%{_javadir}/*.jar

%files jdbc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ott
%{_javadir}/*.zip

%files odbc
%defattr(644,root,root,755)
%doc instantclient_*/ODBC*.htm*
%attr(755,root,root) %{_libdir}/libsqora.so*

%files sqlplus
%defattr(644,root,root,755)
%doc instantclient_*/SQLPLUS_README
%attr(755,root,root) %{_bindir}/sqlplus
%attr(755,root,root) %{_libdir}/libsqlplus.so
%attr(755,root,root) %{_libdir}/libsqlplusic.so
%{_datadir}/sqlplus

%files tools
%defattr(644,root,root,755)
%doc instantclient_*/TOOLS_README
%attr(755,root,root) %{_bindir}/wrc
