#
# Conditional build:
%bcond_with	lite		# build basic lite version of client

%define		otnurl	http://download.oracle.com/otn/linux/instantclient/121010
Summary:	Oracle Database Instant Client
Name:		oracle-instantclient
Version:	12.1.0.1.0
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications/Databases
%ifarch %{ix86}
Source0:	%{otnurl}/instantclient-basic-linux-%{version}.zip
# NoSource0-md5:	7c3b522424713cc8d3814356cf092c02
Source1:	%{otnurl}/instantclient-basiclite-linux-%{version}.zip
# NoSource1-md5:	0d5ec661d9ebfde8880cff5ca1ef9553
Source2:	%{otnurl}/instantclient-sdk-linux-%{version}.zip
# NoSource2-md5:	e33beaaf88256e19f8c59e07d7033159
Source3:	%{otnurl}/instantclient-jdbc-linux-%{version}.zip
# NoSource3-md5:	be0c52004e52448726fb7a4e891c7c98
Source4:	%{otnurl}/instantclient-odbc-linux-%{version}.zip
# NoSource4-md5:	e8ba53efe62b6f3f139a30c55baf78b5
Source5:	%{otnurl}/instantclient-sqlplus-linux-%{version}.zip
# NoSource5-md5:	c3c5bfefce74974f98fd8e72fb2cd44f
Source6:	%{otnurl}/instantclient-tools-linux-%{version}.zip
# NoSource6-md5:	902c817154b5568b2db8c7328d4a10d7
Source7:	%{otnurl}/instantclient-precomp-linux-%{version}.zip
# NoSource7-md5:	4e99435623d82b802d4d95de3598dde7
NoSource:	0
NoSource:	1
NoSource:	2
NoSource:	3
NoSource:	4
NoSource:	5
NoSource:	6
NoSource:	7
%endif
%ifarch %{x8664}
Source10:	%{otnurl}/instantclient-basic-linux.x64-%{version}.zip
# NoSource10-md5:	a555a7f4510e6568e66c45238929f16b
Source11:	%{otnurl}/instantclient-basiclite-linux.x64-%{version}.zip
# NoSource11-md5:	6c712aafb26989699d57c99a3e2bc124
Source12:	%{otnurl}/instantclient-sdk-linux.x64-%{version}.zip
# NoSource12-md5:	e8682f754ea63b9c5f17bd22ba158a75
Source13:	%{otnurl}/instantclient-jdbc-linux.x64-%{version}.zip
# NoSource13-md5:	7b0c4111c6c4a7db062ae961dbc309b6
Source14:	%{otnurl}/instantclient-odbc-linux.x64-%{version}.zip
# NoSource14-md5:	b0e9e3b10ba22b34dbe335426a4fe001
Source15:	%{otnurl}/instantclient-sqlplus-linux.x64-%{version}.zip
# NoSource15-md5:	09d2463277bdbddba36aafc051c5c1b5
Source16:	%{otnurl}/instantclient-tools-linux.x64-%{version}.zip
# NoSource16-md5:	95f2a981ee6515fe31652fb41f7eacbf
Source17:	%{otnurl}/instantclient-precomp-linux.x64-%{version}.zip
# NoSource17-md5:	8ac59bdbb1cb34796c753bdad65e72d9
NoSource:	10
NoSource:	11
NoSource:	12
NoSource:	13
NoSource:	14
NoSource:	15
NoSource:	16
NoSource:	17
%endif
# http://duberga.net/dbd_oracle_instantclient_linux/oracle-instantclient-config
Source20:	oracle-instantclient-config.in
Source21:	oracle-instantclient.pc.in
Patch0:		proc-includes32.patch
Patch1:		proc-includes64.patch
URL:		http://www.oracle.com/technetwork/database/features/instant-client/
BuildRequires:	sed
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		driver_ver	%(echo %{version} | cut -d. -f1)
%define		soname		%(echo %{version} | cut -d. -f1,2)

# verify these with odbc_update_ini.sh
%define		driver_name	"Oracle %{driver_ver}c ODBC driver"
%define		driver_desc	"Oracle ODBC driver for Oracle %{driver_ver}c"

%define		_gcc_sys_inc_dir	%(gcc -print-file-name=include)

# libocci.so - should be linked against libclntsh.so but is not
%define		skip_post_check_so	libclntsh.so.%{soname} libclntshcore.so.%{soname} libocci.so.%{soname} libsqora.so.%{soname}

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
%setup -qcT -b %{?with_lite:1}%{!?with_lite:0} -b 2 -b 3 -b 4 -b 5 -b 6 -b 7
%patch0 -p1
%endif
%ifarch %{x8664}
%setup -qcT -b %{?with_lite:11}%{!?with_lite:10} -b 12 -b 13 -b 14 -b 15 -b 16 -b 17
%patch1 -p1
%endif
mv instantclient_*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus/admin} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_includedir}/oracle/client} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_javadir},/etc}

cp -p *.jar $RPM_BUILD_ROOT%{_javadir}
cp -a *.so* $RPM_BUILD_ROOT%{_libdir}
install -p sqlplus $RPM_BUILD_ROOT%{_bindir}
install -p genezi $RPM_BUILD_ROOT%{_bindir}
install -p adrci $RPM_BUILD_ROOT%{_bindir}
install -p wrc $RPM_BUILD_ROOT%{_bindir}
install -p uidrvci $RPM_BUILD_ROOT%{_bindir}
cp -p glogin.sql $RPM_BUILD_ROOT%{_datadir}/sqlplus/admin

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

cp -p sdk/ottclasses.zip $RPM_BUILD_ROOT%{_javadir}
install -p sdk/ott $RPM_BUILD_ROOT%{_bindir}
install -p sdk/proc* $RPM_BUILD_ROOT%{_bindir}
install -p sdk/rtsora* $RPM_BUILD_ROOT%{_bindir}
cp -a sdk/include/* $RPM_BUILD_ROOT%{_includedir}/oracle/client
cp -a sdk/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

cp -p cobsqlintf.o $RPM_BUILD_ROOT%{_libdir}
cp -a precomp $RPM_BUILD_ROOT%{_libdir}

%{__sed} -i -e "s|@GCC_SYS_INC_DIR@|%{_gcc_sys_inc_dir}|g" \
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

%post	basic -p /sbin/ldconfig
%postun	basic -p /sbin/ldconfig

%post	basiclite -p /sbin/ldconfig
%postun	basiclite -p /sbin/ldconfig

%post	jdbc -p /sbin/ldconfig
%postun	jdbc -p /sbin/ldconfig

%post	sqlplus -p /sbin/ldconfig
%postun	sqlplus -p /sbin/ldconfig

%post odbc
/sbin/ldconfig
# install Orcale driver
/usr/bin/odbcinst -i -d -r <<EOF
[%{driver_name}]
Description = %{driver_desc}
Driver = %{_libdir}/libsqora.so.%{soname}
Setup = 
EOF

%preun odbc
/usr/bin/odbcinst -u -d -n %{driver_name} || :

%postun odbc -p /sbin/ldconfig

%if %{with lite}
%files basiclite
%defattr(644,root,root,755)
%doc BASIC_LITE_README
%attr(755,root,root) %{_libdir}/libociicus.so
%else
%files basic
%defattr(644,root,root,755)
%doc BASIC_README
%attr(755,root,root) %{_libdir}/libociei.so
%endif

# common to basic/basiclite
%config(noreplace) %verify(not md5 mtime size) /etc/tnsnames.ora
%attr(755,root,root) %{_bindir}/adrci
%attr(755,root,root) %{_bindir}/genezi
%attr(755,root,root) %{_bindir}/uidrvci
%attr(755,root,root) %{_libdir}/libocci.so.*
%attr(755,root,root) %{_libdir}/libocijdbc%{driver_ver}.so
%attr(755,root,root) %{_libdir}/libnnz%{driver_ver}.so
%attr(755,root,root) %{_libdir}/libclntsh.so.*
%attr(755,root,root) %{_libdir}/libclntshcore.so.%{soname}
%attr(755,root,root) %{_libdir}/libons.so
%attr(755,root,root) %{_libdir}/liboramysql12.so

%files devel
%defattr(644,root,root,755)
%doc sdk/SDK_README
%attr(755,root,root) %{_bindir}/oracle-instantclient-config
%attr(755,root,root) %{_bindir}/ott
%attr(755,root,root) %{_libdir}/libclntsh.so
%attr(755,root,root) %{_libdir}/libocci.so
%attr(755,root,root) %{_libdir}/libclntshcore.so
%{_pkgconfigdir}/oracle-instantclient.pc
%dir %{_includedir}/oracle
%{_includedir}/oracle/client
%exclude %{_includedir}/oracle/client/oraca.h
%exclude %{_includedir}/oracle/client/sql2oci.h
%exclude %{_includedir}/oracle/client/sqlapr.h
%exclude %{_includedir}/oracle/client/sqlca.h
%exclude %{_includedir}/oracle/client/sqlcpr.h
%exclude %{_includedir}/oracle/client/sqlda.h
%exclude %{_includedir}/oracle/client/sqlkpr.h
%exclude %{_includedir}/oracle/client/sqlucs2.h
%{_examplesdir}/%{name}
%exclude %{_examplesdir}/%{name}/demo_proc*_ic.mk
%exclude %{_examplesdir}/%{name}/*.pc*

%files jdbc
%defattr(644,root,root,755)
%doc JDBC_README
%attr(755,root,root) %{_libdir}/libheteroxa%{driver_ver}.so
%{_javadir}/*.jar

%files jdbc-devel
%defattr(644,root,root,755)
%{_javadir}/*.zip

%files odbc
%defattr(644,root,root,755)
%doc ODBC*.htm*
%attr(755,root,root) %{_libdir}/libsqora.so*

%files sqlplus
%defattr(644,root,root,755)
%doc SQLPLUS_README
%attr(755,root,root) %{_bindir}/sqlplus
%attr(755,root,root) %{_libdir}/libsqlplus.so
%attr(755,root,root) %{_libdir}/libsqlplusic.so
%{_datadir}/sqlplus

%files tools
%defattr(644,root,root,755)
%doc TOOLS_README
%attr(755,root,root) %{_bindir}/wrc

%files precomp
%defattr(644,root,root,755)
%doc PRECOMP_README
%attr(755,root,root) %{_bindir}/proc*
%attr(755,root,root) %{_bindir}/rtsora
%{_libdir}/cobsqlintf.o
%{_libdir}/precomp
%{_examplesdir}/%{name}/demo_proc*_ic.mk
%{_examplesdir}/%{name}/*.pc*

# precomp-devel maybe
%{_includedir}/oracle/client/oraca.h
%{_includedir}/oracle/client/sql2oci.h
%{_includedir}/oracle/client/sqlapr.h
%{_includedir}/oracle/client/sqlca.h
%{_includedir}/oracle/client/sqlcpr.h
%{_includedir}/oracle/client/sqlda.h
%{_includedir}/oracle/client/sqlkpr.h
%{_includedir}/oracle/client/sqlucs2.h
