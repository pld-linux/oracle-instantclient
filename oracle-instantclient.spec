# download requires session cookie; for manual download use:
# http://www.oracle.com/technetwork/topics/linuxsoft-082809.html (ix86)
# http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html (x86_64)
# http://www.oracle.com/technetwork/topics/zlinuxsoft-096525.html (s390/s390x)
# http://www.oracle.com/technetwork/topics/linuxitaniumsoft-087585.html (ia64 - v10.2.0.4)
# http://www.oracle.com/technetwork/topics/linuxpower-101193.html (ppc - v10.2.0.5)
# http://www.oracle.com/technetwork/topics/linuxpower64-092516.html (ppc64 - v10.2.0.5)

%define		otnurl	https://edelivery.oracle.com/akam/otn/linux/instantclient/122010
Summary:	Oracle Database Instant Client
Summary(pl.UTF-8):	Oracle Database Instant Client - klient bazy danych Oracle
Name:		oracle-instantclient
Version:	12.2.0.1.0
Release:	1
License:	OTN (proprietary, non-distributable)
Group:		Applications/Databases
%ifarch %{ix86}
Source0:	%{otnurl}/instantclient-basic-linux-%{version}.zip
# NoSource0-md5:	afc84c453dd143d6138baa1faf3e3a52
Source1:	%{otnurl}/instantclient-basiclite-linux-%{version}.zip
# NoSource1-md5:	dc493bcf009b371f302f8360b275bad0
Source2:	%{otnurl}/instantclient-sdk-linux-%{version}.zip
# NoSource2-md5:	a53172101846638c9e8c32af63991130
Source3:	%{otnurl}/instantclient-jdbc-linux-%{version}.zip
# NoSource3-md5:	24df104cc59254ab4928d4eb3a19cbd3
Source4:	%{otnurl}/instantclient-odbc-linux-%{version}.zip
# NoSource4-md5:	6be26ef53189faa8a622fd0a80bb7473
Source5:	%{otnurl}/instantclient-sqlplus-linux-%{version}.zip
# NoSource5-md5:	3c9a3ec6172f620a065ee8bc68c408bf
Source6:	%{otnurl}/instantclient-tools-linux-%{version}.zip
# NoSource6-md5:	d00f4a31ed12cf19eb38c8ce37b6e772
Source7:	%{otnurl}/instantclient-precomp-linux-%{version}.zip
# NoSource7-md5:	0e70ac53b10da7f137be01e99d9c8de3
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
# NoSource10-md5:	d9639092e3dea2e023272e52e2bd42da
Source11:	%{otnurl}/instantclient-basiclite-linux.x64-%{version}.zip
# NoSource11-md5:	b024039f518975f5a5b6473130c74e43
Source12:	%{otnurl}/instantclient-sdk-linux.x64-%{version}.zip
# NoSource12-md5:	077fa2f215185377ccb670de9ca1678f
Source13:	%{otnurl}/instantclient-jdbc-linux.x64-%{version}.zip
# NoSource13-md5:	3e6cdc6686b44160a8a5e4af0cacf5fd
Source14:	%{otnurl}/instantclient-odbc-linux.x64-%{version}.zip
# NoSource14-md5:	a047b8e637624b76b80d07fd8a9f1baf
Source15:	%{otnurl}/instantclient-sqlplus-linux.x64-%{version}.zip
# NoSource15-md5:	93ae87df1d08bb31da57443a416edc8c
Source16:	%{otnurl}/instantclient-tools-linux.x64-%{version}.zip
# NoSource16-md5:	5e258c34f947c31f0cf0e6322da8fe2c
Source17:	%{otnurl}/instantclient-precomp-linux.x64-%{version}.zip
# NoSource17-md5:	30e571eff9003522d13bde4298461476
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
Source20:	%{name}-config.in
Source21:	%{name}.pc.in
Source22:	tnsnames.ora
Source23:	sqlnet.ora
Patch0:		proc-includes32.patch
Patch1:		proc-includes64.patch
URL:		http://www.oracle.com/technetwork/database/features/instant-client/
BuildRequires:	unzip
Suggests:	%{name}-basic
Suggests:	%{name}-basiclite
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		driver_ver	%(echo %{version} | cut -d. -f1)
%define		soname		12.1

# verify these with odbc_update_ini.sh
%define		driver_name	"Oracle %{driver_ver}c ODBC driver"
%define		driver_desc	"Oracle ODBC driver for Oracle %{driver_ver}c"

%define		_gcc_sys_inc_dir	%(gcc -print-file-name=include)

# libocci.so - should be linked against libclntsh.so but is not
%define		skip_post_check_so	libclntsh.so.%{soname} libclntshcore.so.%{soname} libocci.so.%{soname} libsqora.so.%{soname}

# don't generate deps for Intel Cobol Compiler
%define		_noautoreq		^libcob.*.so

%description
Oracle Database Instant Client Package.

%description -l pl.UTF-8
Pakiet Oracle Database Instant Client - klient bazy danych Oracle.

%package basic
Summary:	Oracle Database Instant Client - Basic
Summary(pl.UTF-8):	Oracle Database Instant Client - wersja Basic
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Conflicts:	oracle-instantclient < 12.1.0.1.0-0.4

%description basic
All files required to run OCI, and OCCI, and JDBC-OCI applications.

%description basic -l pl.UTF-8
Wszystkie pliki wymagane do uruchamiania aplikacji OCI, OCCI oraz
JDBC-OCI.

%package basiclite
Summary:	Oracle Database Instant Client - Basic Lite
Summary(pl.UTF-8):	Oracle Database Instant Client - wersja Basic Lite
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Conflicts:	oracle-instantclient < 12.1.0.1.0-0.4

%description basiclite
All files required to run OCI, and OCCI, and JDBC-OCI applications.

This package contains only English error messages and Unicode, ASCII,
and Western European character set support.

%description basiclite -l pl.UTF-8
Wszystkie pliki wymagane do uruchamiania aplikacji OCI, OCCI oraz
JDBC-OCI.

Ten pakiet zawiera wyłącznie komunikaty błędów po angielsku oraz
obsługę zestawów znaków Unicode, ASCII oraz zachodnioeuropejskiego.

%package devel
Summary:	SDK for Oracle Database Instant Client
Summary(pl.UTF-8):	SDK dla bibliotek Oracle Database Instant Client
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Additional header files and an example makefile for developing Oracle
applications with Instant Client.

%description devel -l pl.UTF-8
Dodatkowe pliki nagłówkowe oraz przykładowy plik makefile do tworzenia
aplikacji Oracle przy użyciu Instant Clienta.

%package -n java-jdbc-%{name}
Summary:	JDBC for Oracle Database Instant Client
Summary(pl.UTF-8):	Biblioteka JDBC dla Oracle Database Instant Clienta
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}
Obsoletes:	oracle-instantclient-jdbc < 12.1.0.1.0-0.6

%description -n java-jdbc-%{name}
Oracle Database Instant Client Package - JDBC.

Support for JDBC-OCI, XA, Internationalization, and RowSet operations
under JDBC.

%description -n java-jdbc-%{name} -l pl.UTF-8
Pakiet Oracle Database Instant Client - biblioteka JDBC.

Obsługa JDBC-OCI, XA, lokalizacji oraz operacji RowSet pod JDBC.

%package -n java-jdbc-%{name}-devel
Summary:	JDBC for Oracle Database Instant Client development files
Summary(pl.UTF-8):	Pliki programistyczne JDBC dla Oracle Database Instant Clienta
Group:		Development/Languages/Java
Requires:	java-jdbc-%{name} = %{version}-%{release}
Obsoletes:	oracle-instantclient-jdbc-devel < 12.1.0.1.0-0.6

%description -n java-jdbc-%{name}-devel
Oracle Database Instant Client Package - JDBC development files.

%description -n java-jdbc-%{name}-devel -l pl.UTF-8
Pakiet Oracle Database Instant Client - pliki programistyczne JDBC.

%package odbc
Summary:	ODBC for Oracle Database Instant Client
Summary(pl.UTF-8):	Biblioteka ODBC dla Oracle Database Instant Clienta
Group:		Libraries
Requires(post,preun):	/usr/bin/odbcinst
Requires:	%{name} = %{version}-%{release}
Requires:	unixODBC

%description odbc
Oracle ODBC Instant Client for Linux complies with ODBC 3.52
specifications. It is based on features of Oracle %{version} ODBC
driver for Windows, without the need for a traditional ORACLE_HOME
installation.

%description odbc -l pl.UTF-8
Oracle ODBC Instant Client dla Linuksa jest zgodny ze specyfikacją
ODBC 3.52. Jest oparty na możliwościach sterownika ODBC dla Oracle
%{version}, bez potrzeby tradycyjnej instalacji ORACLE_HOME.

%package sqlplus
Summary:	Oracle Database Client - SQL*Plus
Summary(pl.UTF-8):	Klient bazy danych Oracla - SQL*Plus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description sqlplus
Oracle Database Instant Client Package - SQL*Plus.

Additional libraries and executable for running SQL*Plus with Instant
Client.

%description sqlplus -l pl.UTF-8
Pakiet Oracle Database Instant Client - SQL*Plus.

Dodatkowe biblioteki i program do uruchamiania SQL*Plus wraz z Instant
Clientem.

%package tools
Summary:	Oracle Database Workload Replay Client
Summary(pl.UTF-8):	Narzędzie Oracle Database Workload Replay Client
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description tools
Oracle Database Instant Client Package - WRC.

WRC - Workload Replay Client used to replay workload for RAT's DB
Replay Feature.

%description tools -l pl.UTF-8
Pakiet Oracle Database Instant Client - WRC.

WRC (Workload Replay Client) służy do odtwarzania danych dla RAT DB
Replay.

%package precomp
Summary:	Oracle Database Client - Precompiler
Summary(pl.UTF-8):	Prekompilator klienta bazy danych Oracle
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description precomp
PRECOMP Instant Client (IC) Package contains following components:
- "proc" binary to precompile a Pro*C application
- "procob" binary to precompile a Pro*COBOL application
- sample configuration files, demo programs and demo make files for
  building proc and procob demos and in general any Pro*C/Pro*COBOL
  application.

%description precomp -l pl.UTF-8
Pakiet PRECOMP Instant Client (IC) zawiera następujące komponenty:
- program "proc" do prekompilacji aplikacji Pro*C
- program "procob" do prekompilacji aplikacji Pro*COBOL
- przykładowe pliki konfiguracyjne, programy demonstracyjne oraz pliki
  makefile dla programów demonstracyjnych proc i procob, a także
  dowolnych aplikacji Pro*C/Pro*COBOL

%prep
%define	__unzip unzip -n
%ifarch %{ix86}
%setup -qcT -b 0 -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7
%patch0 -p1
%endif
%ifarch %{x8664}
%setup -qcT -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 17
%patch1 -p1
%endif
mv instantclient_*/* .

mv help/us help_us
mv help/ja help_ja

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus/admin} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_includedir}/oracle/client} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_javadir},%{_sysconfdir}}

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

cp -p %{SOURCE22} $RPM_BUILD_ROOT%{_sysconfdir}/tnsnames.ora
cp -p %{SOURCE23} $RPM_BUILD_ROOT%{_sysconfdir}/sqlnet.ora
# make it load without ORACLE_HOME env
install -d $RPM_BUILD_ROOT%{_libdir}/network/admin
ln -s %{_sysconfdir}/sqlnet.ora $RPM_BUILD_ROOT%{_libdir}/network/admin/sqlnet.ora

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

%post	-n java-jdbc-%{name} -p /sbin/ldconfig
%postun	-n java-jdbc-%{name} -p /sbin/ldconfig

%post	sqlplus -p /sbin/ldconfig
%postun	sqlplus -p /sbin/ldconfig

%post odbc
/sbin/ldconfig
# install Oracle driver
/usr/bin/odbcinst -i -d -r <<EOF
[%{driver_name}]
Description = %{driver_desc}
Driver = %{_libdir}/libsqora.so.%{soname}
Setup =
EOF

%preun odbc
/usr/bin/odbcinst -u -d -n %{driver_name} || :

%postun odbc -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tnsnames.ora
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sqlnet.ora
%attr(755,root,root) %{_bindir}/adrci
%attr(755,root,root) %{_bindir}/genezi
%attr(755,root,root) %{_bindir}/uidrvci
# libnnz.so: Security library
%attr(755,root,root) %{_libdir}/libnnz%{driver_ver}.so
%attr(755,root,root) %{_libdir}/libons.so
# libclntsh.so, libclntshcore.so: Client Code Library and data shared library.
%attr(755,root,root) %{_libdir}/libclntsh.so.*
%attr(755,root,root) %{_libdir}/libclntshcore.so.%{soname}

# subpackage these (not directly needed by php-ext):
# libocci.so: OCCI (Oracle C++ Call Interface) Library
%attr(755,root,root) %{_libdir}/libocci.so.*

%ifarch %{x8664}
%attr(755,root,root) %{_libdir}/libipc1.so
%attr(755,root,root) %{_libdir}/libmql1.so
%endif

# liboramysql.so: MySQL Client Library Driver for Oracle Database,
# drop-in replacement for MySQL Commercial Connector/C 6.0 client library.
%attr(755,root,root) %{_libdir}/liboramysql%{driver_ver}.so

# parent dirs for sqlnet.ora
%dir %{_libdir}/network
%dir %{_libdir}/network/admin
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/network/admin/sqlnet.ora

%files basiclite
%defattr(644,root,root,755)
%doc BASIC_LITE_README
# libociicus.so: OCI Instant Client data shared library (English only)
%attr(755,root,root) %{_libdir}/libociicus.so

%files basic
%defattr(644,root,root,755)
%doc BASIC_README
# libociei.so: OCI Instant Client data shared library
%attr(755,root,root) %{_libdir}/libociei.so

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

%files -n java-jdbc-%{name}
%defattr(644,root,root,755)
%doc JDBC_README
%attr(755,root,root) %{_libdir}/libheteroxa%{driver_ver}.so
# libocijdbc12.so: OCI Instant Client JDBC Library
%attr(755,root,root) %{_libdir}/libocijdbc%{driver_ver}.so
%{_javadir}/ojdbc8.jar
%{_javadir}/orai18n-mapping.jar
%{_javadir}/orai18n.jar
%{_javadir}/xstreams.jar

%files -n java-jdbc-%{name}-devel
%defattr(644,root,root,755)
%{_javadir}/ottclasses.zip

%files odbc
%defattr(644,root,root,755)
%doc ODBC*.html
%doc help_us
%doc %lang(ja) help_ja
%attr(755,root,root) %{_libdir}/libsqora.so.%{soname}
%attr(755,root,root) %{_libdir}/libsqora.so

%files sqlplus
%defattr(644,root,root,755)
%doc SQLPLUS_README
%attr(755,root,root) %{_bindir}/sqlplus
# libsqlplus.so: SQL*Plus library
%attr(755,root,root) %{_libdir}/libsqlplus.so
# libsqlplusic.so: SQL*Plus data shared library
%attr(755,root,root) %{_libdir}/libsqlplusic.so
%dir %{_datadir}/sqlplus
%dir %{_datadir}/sqlplus/admin
%{_datadir}/sqlplus/admin/glogin.sql

%files tools
%defattr(644,root,root,755)
%doc TOOLS_README
%attr(755,root,root) %{_bindir}/wrc

%files precomp
%defattr(644,root,root,755)
%doc PRECOMP_README
%attr(755,root,root) %{_bindir}/proc
%attr(755,root,root) %{_bindir}/procob
%attr(755,root,root) %{_bindir}/rtsora
%{_libdir}/cobsqlintf.o
%dir %{_libdir}/precomp
%dir %{_libdir}/precomp/admin
%{_libdir}/precomp/admin/pcscfg.cfg
%{_libdir}/precomp/admin/pcbcfg.cfg
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
