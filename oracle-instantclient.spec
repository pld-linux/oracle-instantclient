#
# Conditional build:
%bcond_with	lite		# build basic lite version of client

%define		x86ver		11.2.0.2.0
%define		x8664ver	11.2.0.2.0

Summary:	Oracle Database Instant Client
Name:		oracle-instantclient
Version:	11.2.0.2.0
Release:	1
License:	OTN (proprietary, non-distributable)
Group:		Applications/Databases
Source0:	instantclient-basic-linux32-%{x86ver}.zip
# NoSource0-md5:	efa27cd21e6f078c27838232cb836b25
Source1:	instantclient-basiclite-linux32-%{x86ver}.zip
# NoSource1-md5:	4a5faca63686ba46eb01876267c06872
Source2:	instantclient-sdk-linux32-%{x86ver}.zip
# NoSource2-md5:	a0034b6f3ea18480d9857de7777a515e
Source3:	instantclient-jdbc-linux32-%{x86ver}.zip
# NoSource3-md5:	b9e46ce5dba8f7b75616a5258dce30c7
Source4:	instantclient-odbc-linux32-%{x86ver}.zip
# NoSource4-md5:	ac96b2f710ffe12117347c0a8c36ddcd
Source5:	instantclient-sqlplus-linux32-%{x86ver}.zip
# NoSource5-md5:	6d6912d016d42fcc36335275885c781f
Source6:	instantclient-tools-linux32-%{x86ver}.zip
# NoSource6-md5:	1c8b2c9332372b3367685bdfcf2629c4
Source7:	instantclient-precomp-linux32-%{x86ver}.zip
# NoSource7-md5:	e495288a85fe7e40e74e90dd97cad04c
Source10:	instantclient-basic-linux-x86-64-%{x8664ver}.zip
# NoSource10-md5:	7507de5158e48d7a16def5235a1b4171
Source11:	instantclient-basiclite-linux-x86-64-%{x8664ver}.zip
# NoSource11-md5:	9fa61d0216fdf64af1b5247734f2f291
Source12:	instantclient-sdk-linux-x86-64-%{x8664ver}.zip
# NoSource12-md5:	201ed479c9cfd3905cecbd213c656331
Source13:	instantclient-jdbc-linux-x86-64-%{x8664ver}.zip
# NoSource13-md5:	2f101569da1824eba9d9cdd393dce2ff
Source14:	instantclient-odbc-linux-x86-64-%{x8664ver}.zip
# NoSource14-md5:	161daea9c01f3c2e027d36d7975f0044
Source15:	instantclient-sqlplus-linux-x86-64-%{x8664ver}.zip
# NoSource15-md5:	805460a9d387c53c615e64d026bf15b9
Source16:	instantclient-tools-linux-x86-64-%{x8664ver}.zip
# NoSource16-md5:	bbe33d3fb08f226c3f0c3ca57a4ed2c2
Source17:	instantclient-precomp-linux-x86-64-%{x8664ver}.zip
# NoSource17-md5:	e79b5c703e8bbf5de62cf6d0061f342f
# http://duberga.net/dbd_oracle_instantclient_linux/oracle-instantclient-config
Source20:	oracle-instantclient-config.in
Source21:	oracle-instantclient.pc.in
Patch0:		%{name}-proc-includes.patch
NoSource:	0
NoSource:	1
NoSource:	2
NoSource:	3
NoSource:	4
NoSource:	5
NoSource:	6
NoSource:	7
NoSource:	10
NoSource:	11
NoSource:	12
NoSource:	13
NoSource:	14
NoSource:	15
NoSource:	16
NoSource:	17
URL:		http://www.oracle.com/technetwork/database/features/instant-client/
BuildRequires:	sed
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gcc_sys_inc_dir	%(gcc -print-file-name=include)

# this should be linked against libclntsh.so but is not
%define		skip_post_check_so	libocci.so.*
# don't generate deps for Intel Cobol Compiler
%define		_noautoreq		^libcob.*.so

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

%package precomp
Summary:	Oracle Database Client - Precompiler
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description precomp
Oracle Database Instant Client Package - Precompiler.
Additional files for "proc" binary and related files
to precompile a Pro*C application and demo.

%prep
%ifarch %{ix86}
%setup -q -c -T -b %{?with_lite:1}%{!?with_lite:0} -b 2 -b 3 -b 4 -b 5 -b 6 -b 7
%endif

%ifarch %{x8664}
%setup -q -c -T -b %{?with_lite:11}%{!?with_lite:10} -b 12 -b 13 -b 14 -b 15 -b 16 -b 17
%endif

%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus/admin} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_includedir}/oracle/client} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_javadir},/etc}

cd instantclient_*

install -p *.jar $RPM_BUILD_ROOT%{_javadir}
install -p *.so* $RPM_BUILD_ROOT%{_libdir}
install -p sqlplus $RPM_BUILD_ROOT%{_bindir}
install -p genezi $RPM_BUILD_ROOT%{_bindir}
install -p adrci $RPM_BUILD_ROOT%{_bindir}
install -p wrc $RPM_BUILD_ROOT%{_bindir}
install -p uidrvci $RPM_BUILD_ROOT%{_bindir}
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
install -p sdk/proc* $RPM_BUILD_ROOT%{_bindir}
install -p sdk/rtsora* $RPM_BUILD_ROOT%{_bindir}
install -p sdk/include/* $RPM_BUILD_ROOT%{_includedir}/oracle/client
install -p sdk/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install -p cobsqlintf.o $RPM_BUILD_ROOT%{_libdir}
cp -a precomp $RPM_BUILD_ROOT%{_libdir}

%{__sed} -i -e "s|@@GCC_SYS_INC_DIR@@|%{_gcc_sys_inc_dir}|g" \
	$RPM_BUILD_ROOT%{_libdir}/precomp/admin/pcscfg.cfg

cat <<EOF >$RPM_BUILD_ROOT/etc/tnsnames.ora
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
%attr(755,root,root) %{_bindir}/uidrvci
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
%attr(755,root,root) %{_bindir}/uidrvci
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
%exclude %{_includedir}/oracle/client/oraca.h
%exclude %{_includedir}/oracle/client/sql2oci.h
%exclude %{_includedir}/oracle/client/sqlapr.h
%exclude %{_includedir}/oracle/client/sqlca.h
%exclude %{_includedir}/oracle/client/sqlcpr.h
%exclude %{_includedir}/oracle/client/sqlda.h
%exclude %{_includedir}/oracle/client/sqlkpr.h
%exclude %{_includedir}/oracle/client/sqlucs2.h
%{_javadir}/*.zip
%{_examplesdir}/%{name}
%exclude %{_examplesdir}/%{name}/demo_proc*_ic.mk
%exclude %{_examplesdir}/%{name}/*.pc*

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

%files precomp
%defattr(644,root,root,755)
%doc instantclient_*/PRECOMP_README
%attr(755,root,root) %{_bindir}/proc*
%attr(755,root,root) %{_bindir}/rtsora
%{_libdir}/cobsqlintf.o
%{_libdir}/precomp
%{_examplesdir}/%{name}/demo_proc*_ic.mk
%{_examplesdir}/%{name}/*.pc*
