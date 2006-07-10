#
# Conditional build:
%bcond_without	grsec_minimal	# don't build grsecurity (minimal subset: proc,link,fifo,shm)
%bcond_with	verbose		# verbose build (V=1)

%{?debug:%define with_verbose 1}

%ifarch %{ix86} ppc
%define		have_isa	1
%else
%define		have_isa	0
%endif

## Program required by kernel to work.
%define		_binutils_ver		2.12.1
%define		_util_linux_ver		2.10o
%define		_module_init_tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_reiser4progs_ver	1.0.0
%define		_xfsprogs_ver		2.6.0
%define		_pcmcia_cs_ver		3.1.21
%define		_pcmciautils_ver	004
%define		_quota_tools_ver	3.09
%define		_ppp_ver		1:2.4.0
%define		_isdn4k_utils_ver	3.1pre1
%define		_nfs_utils_ver		1.0.5
%define		_procps_ver		3.2.0
%define		_oprofile_ver		0.9
%define		_udev_ver		071


%define		_netfilter_snap		20060504
%define		_nf_hipac_ver		0.9.1

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22

%define		squashfs_version	3.0
%define		suspend_version		2.2.7

%define		xen_version		3.0.2

%ifarch ppc
%define		alt_kernel	ppcrcd
%else
%define		alt_kernel	rescuecd
%endif

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel-%{alt_kernel}
%define		_basever	2.6.17
%define		_postver	.4
%define		_rel		0.2
Version:	%{_basever}%{_postver}
Release:	%{_rel}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
%define		_rc	%{nil}
#define		_rc	-rc6
#Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/linux-%{_basever}%{_rc}.tar.bz2
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{_basever}.tar.bz2
# Source0-md5:	37ddefe96625502161f075b9d907f21e
%if "%{_postver}" != "%{nil}"
Source1:	http://www.kernel.org/pub/linux/kernel/v2.6/patch-%{version}.bz2
# Source1-md5:	c3b9e8e7b63d6273c5476a999a3b6280
%endif
Source2:	kernel-rcd-ppclibs.Makefile
Source3:	kernel-desktop-autoconf.h
Source4:	kernel-desktop-config.h
Source5:	kernel-rcd-module-build.pl

Source10:	kernel-rcd-i386.config
Source11:	kernel-rcd-x86_64.config
Source12:	kernel-rcd-ppc.config

###
#	Patches
###

Patch1:		kernel-rcd-grsec-minimal.patch

# filesystems
Patch10:	kernel-desktop-reiser4.patch
Patch11:	kernel-desktop-squashfs.patch
Patch12:	kernel-rcd-squashfs-lzma.patch

# hardware
Patch20:	kernel-desktop-tahoe9xx.patch
Patch21:	kernel-desktop-sk98lin.patch
Patch23:	kernel-desktop-hdaps_protect.patch

# console
Patch30:	kernel-rcd-fbsplash.patch

########	netfilter snap
## base
Patch40:	kernel-desktop-pom-ng-IPV4OPTSSTRIP.patch
Patch41:	kernel-desktop-pom-ng-connlimit.patch
Patch42:	kernel-desktop-pom-ng-expire.patch
Patch43:	kernel-desktop-pom-ng-fuzzy.patch
Patch44:	kernel-desktop-pom-ng-ipv4options.patch
Patch45:	kernel-desktop-pom-ng-nth.patch
Patch46:	kernel-desktop-pom-ng-osf.patch
Patch47:	kernel-desktop-pom-ng-psd.patch
Patch48:	kernel-desktop-pom-ng-quota.patch
Patch49:	kernel-desktop-pom-ng-random.patch
Patch50:	kernel-desktop-pom-ng-set.patch
Patch51:	kernel-desktop-pom-ng-time.patch
Patch52:	kernel-desktop-pom-ng-u32.patch

## extra
Patch60:	kernel-desktop-pom-ng-ACCOUNT.patch
Patch61:	kernel-desktop-pom-ng-IPMARK.patch
Patch62:	kernel-desktop-pom-ng-ROUTE.patch
Patch63:	kernel-desktop-pom-ng-TARPIT.patch
Patch64:	kernel-desktop-pom-ng-account.patch
Patch65:	kernel-desktop-pom-ng-ipp2p.patch
Patch66:	kernel-desktop-pom-ng-rpc.patch
########	End netfilter

# net software
Patch70:	kernel-desktop-imq2.patch
Patch71:	kernel-desktop-esfq.patch
Patch72:	kernel-desktop-atm-vbr.patch
Patch73:	kernel-desktop-atmdd.patch

# fixes
Patch80:	kernel-desktop-sco-mtu.patch
Patch81:	kernel-desktop-fbcon-margins.patch
Patch82:	kernel-desktop-static-dev.patch
Patch100:	kernel-desktop-small_fixes.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 3:2.14.90.0.7
BuildRequires:	diffutils
BuildRequires:	gcc >= 5:3.2
BuildRequires:	module-init-tools
# for hostname command
BuildRequires:	net-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.217
Autoreqprov:	no
Requires:	coreutils
Requires:	module-init-tools >= 0.9.9
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(realtime-lsm) = 0.1.1
Provides:	kernel-misc-fuse
Provides:	kernel-net-hostap = 0.4.4
Provides:	kernel-net-ieee80211
Provides:	kernel-net-ipp2p = 1:0.8.0
Provides:	kernel-net-ipw2100 = 1.1.3
Provides:	kernel-net-ipw2200 = 1.0.8
Provides:	module-info
# fake, as we have no time to fix rpm
Provides:	uname(release) = %{version}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
Conflicts:	oprofile < %{_oprofile_ver}
Conflicts:	ppp < %{_ppp_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	udev < %{_udev_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
ExclusiveArch:	%{ix86} %{x8664} ppc
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ver		%{version}_%{alt_kernel}
%define		ver_rel		%{version}_%{alt_kernel}-%{release}

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Packet enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeß-Management, Geräte Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un système d'exploitation Linux. Le noyau traite les
fonctions basiques d'un système d'exploitation: allocation mémoire,
allocation de process, entrée/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j±dro Linuksa niezbêdne do prawid³owego dzia³ania
Twojego komputera. Zawiera w sobie sterowniki do sprzêtu znajduj±cego
siê w komputerze, takiego jak sterowniki dysków itp.

%package libs
Summary:	Libraries for preparing bootable kernel on PowerPCs
Summary(pl):	Biblioteki do przygotowania bootowalnego j±dra dla PowerPC
Group:		Base/Kernel
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description libs
Libraries for preparing bootable kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description libs -l pl
Biblioteki do przygotowania bootowalnego j±dra dla PowerPC. Skrypt
mkvmlinuz mo¿e byæ do tego przydatny.

%package vmlinux
Summary:	vmlinux - uncompressed kernel image
Summary(de):	vmlinux - dekompressiertes Kernel Bild
Summary(pl):	vmlinux - rozpakowany obraz j±dra
Group:		Base/Kernel

%description vmlinux
vmlinux - uncompressed kernel image.

%description vmlinux -l de
vmlinux - dekompressiertes Kernel Bild.

%description vmlinux -l pl
vmlinux - rozpakowany obraz j±dra.

%package net-netfilter
Summary:	Netfilter kernel modules
Summary(de):	Netfilter Kernel Treiber
Summary(pl):	Modu³y Netfiltera
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	kernel(nf-hipac) = %{_nf_hipac_ver}
Autoreqprov:	no

%description net-netfilter
Netfilter kernel modules (%{_netfilter_snap}).

%description net-netfilter -l de
Netfilter Kernel Treiber (%{_netfilter_snap}).

%description net-netfilter -l pl
Modu³y Netfiltera (%{_netfilter_snap}).

%package pcmcia
Summary:	PCMCIA modules
Summary(de):	PCMCIA Module
Summary(pl):	Modu³y PCMCIA
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel(pcmcia)
Provides:	kernel-pcmcia = %{pcmcia_version}
Conflicts:	pcmcia-cs < %{_pcmcia_cs_ver}
Conflicts:	pcmciautils < %{_pcmciautils_ver}
Autoreqprov:	no

%description pcmcia
PCMCIA modules (%{pcmcia_version}).

%description pcmcia -l de
PCMCIA Module (%{pcmcia_version})

%description pcmcia -l pl
Modu³y PCMCIA (%{pcmcia_version}).

%package headers
summary:	header files for the linux kernel
summary(de):	header dateien für den linux-kernel
summary(pl):	pliki nag³ówkowe j±dra linuksa
group:		development/building
provides:	kernel-headers = %{epoch}:%{version}-%{release}
provides:	kernel-headers(agpgart) = %{version}
provides:	kernel-headers(alsa-drivers)
provides:	kernel-headers(bridging) = %{version}
provides:	kernel-headers(netfilter) = %{_netfilter_snap}
provides:	kernel-headers(reiserfs) = %{version}
autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%description headers -l de
Dies sind die C Header Dateien für den Linux-Kernel, die definierte
Strukturen und Konstante beinhalten die beim rekompilieren des Kernels
oder bei Kernel Modul kompilationen gebraucht werden.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbêdne do rekompilacji j±dra
oraz budowania modu³ów j±dra.

%package module-build
Summary:	Development files for building kernel modules
Summary(de):	Development Dateien die beim Kernel Modul kompilationen gebraucht werden
Summary(pl):	Pliki s³u¿±ce do budowania modu³ów j±dra
Group:		Development/Building
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-module-build = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%description module-build -l de
Development Dateien des Linux-Kernels die beim kompilieren externer
Kernel Module gebraucht werden.

%description module-build -l pl
Pliki ze drzewa ¼róde³ j±dra potrzebne do budowania modu³ów j±dra
Linuksa z zewnêtrznych pakietów.

%package source
Summary:	Kernel source tree
Summary(de):	Der Kernel Quelltext
Summary(pl):	Kod ¼ród³owy j±dra Linuksa
Group:		Development/Building
Requires:	%{name}-module-build = %{epoch}:%{version}-%{release}
Provides:	kernel-source = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l de
Das Kernel-Source-Packet enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu kompilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu kompilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nécessaires pour compiler la plupart des
programmes C, car il dépend de constantes définies dans le code
source. Les sources peuvent être aussi utilisée pour compiler un noyau
personnalisé pour avoir de meilleures performances sur des matériels
particuliers.

%description source -l pl
Pakiet zawiera kod ¼ród³owy j±dra systemu.

%package doc
Summary:	Kernel documentation
Summary(de):	Kernel Dokumentation
Summary(pl):	Dokumentacja do j±dra Linuksa
Group:		Documentation
Provides:	kernel-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
Documentation directory.

%description doc -l de
Dies ist die Kernel Dokumentation wie sie im 'Documentation' Verzeichniss
vorgefunden werden kann.

%description doc -l pl
Pakiet zawiera dokumentacjê do j±dra Linuksa pochodz±c± z katalogu
Documentation.

%prep
%setup -q -n linux-%{_basever}%{_rc}

%if "%{_postver}" != "%{nil}"
%{__bzip2} -dc %{SOURCE1} | patch -p1 -s
%endif

install %{SOURCE2} Makefile.ppclibs

# grsecurity
%if %{with grsec_minimal}
%patch1 -p1
%endif

# filesystems
%patch10 -p1
%patch11 -p1
%patch12 -p1

# hardware
%patch20 -p1
%patch21 -p1
%patch23 -p1

# fbsplash is used in ppcrcd
%ifarch ppc
%patch30 -p1
%endif

### netfilter
# base
%if 0
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1

## extra
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%endif
### end of netfilter

# net software
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1

# fixes
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch100 -p1

sed -i -e '/select INPUT/d' net/bluetooth/hidp/Kconfig

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{_postver}_%{alt_kernel}#g' Makefile
echo "-%{release}" > localversion

%build
%if "%{_target_base_arch}" != "%{_arch}"
	CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
	%if "%{_arch}" == "x86_64" && "%_target_base_arch}" == "i386"
	CrossOpts="ARCH=%{_target_base_arch}"
	%endif
%else
	CrossOpts=""
%endif

rm -f include/linux/autoconf.h
%{__make} $CrossOpts mrproper

cat $RPM_SOURCE_DIR/kernel-rcd-%{_target_base_arch}.config > .config


# BuildKernel

%{__make} $CrossOpts clean

%{__make} $CrossOpts include/linux/version.h \
	%{?with_verbose:V=1}

%{__make} $CrossOpts \
	%{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT
umask 022

%if "%{_target_base_arch}" != "%{_arch}"
	CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
	DepMod=/bin/true
	export DEPMOD=/bin/true
	%if "%{_arch}" == "x86_64" && "%{_target_base_arch}" == "i386"
	CrossOpts="ARCH=%{_target_base_arch}"
	DepMod=/sbin/depmod
	unset DEPMOD
	%endif
%else
	CrossOpts=""
	DepMod=/sbin/depmod
%endif

# Install files in /boot
mkdir -p $RPM_BUILD_ROOT/boot
install System.map $RPM_BUILD_ROOT/boot/System.map-%{ver_rel}
%ifarch %{ix86} %{x8664}
	install arch/%{_target_base_arch}/boot/bzImage \
		$RPM_BUILD_ROOT/boot/vmlinuz-%{ver_rel}
%endif

%ifarch ppc
	install vmlinux.strip $RPM_BUILD_ROOT/boot/vmlinuz-%{ver_rel}
	%{__make} -f Makefile.ppclibs install \
		DESTDIR=$RPM_BUILD_ROOT/boot/libs-%{ver_rel}
%endif
install vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{ver_rel}

# Install modules
%{__make} $CrossOpts modules_install \
	%{?with_verbose:V=1} \
	DEPMOD=$DepMod \
	INSTALL_MOD_PATH=$RPM_BUILD_ROOT \
	KERNELRELEASE=%{ver_rel}

if [ -z "$CrossOpts" ]; then
	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	/sbin/depmod --basedir $RPM_BUILD_ROOT -ae \
		-F $RPM_BUILD_ROOT/boot/System.map-%{ver_rel} -r %{ver_rel} \
		|| echo
else
	touch $RPM_BUILD_ROOT/lib/modules/%{ver_rel}/modules.dep
fi

rm -f $RPM_BUILD_ROOT/lib/modules/%{ver_rel}/build
ln -sf %{_prefix}/src/linux-%{ver} \
	$RPM_BUILD_ROOT/lib/modules/%{ver_rel}/build
install -d $RPM_BUILD_ROOT/lib/modules/%{ver_rel}/{cluster,misc}

install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{ver_rel}


# Install Source
install -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver}
ln -sf linux-%{ver} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{alt_kernel}

find . -maxdepth 1 ! -name "build-done" ! -name "." -exec cp -a "{}" "$RPM_BUILD_ROOT/usr/src/linux-%{ver}/" ";"

find $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver} '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

install	include/linux/autoconf.h \
	$RPM_BUILD_ROOT/usr/src/linux-%{ver}/include/linux/autoconf-up.h
install	.config \
	$RPM_BUILD_ROOT/usr/src/linux-%{ver}/config-up
install Module.symvers \
	$RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver}/Module.symvers-up

%{__make} -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver} $CrossOpts mrproper
%{__make} -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver} $CrossOpts include/linux/version.h
install %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver}/include/linux/autoconf.h
install %{SOURCE4} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver}/include/linux/config.h

# collect module-build files and directories
perl %{SOURCE5} %{_prefix}/src/linux-%{ver} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{ver}

%clean
rm -rf $RPM_BUILD_ROOT

%preun
rm -f /lib/modules/%{ver_rel}/modules.*

# no %post here, everything must be done manually

%post headers
rm -f /usr/src/linux-%{alt_kernel}
ln -snf linux-%{ver} /usr/src/linux-%{alt_kernel}

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux-%{alt_kernel} ]; then
		if [ "`ls -l %{_prefix}/src/linux-%{alt_kernel} | awk '{ print $10 }'`" = "linux-%{ver}" ]; then
			rm -f %{_prefix}/src/linux-%{alt_kernel}
		fi
	fi
fi

%files
%defattr(644,root,root,755)
/boot/vmlinuz-%{ver_rel}
/boot/System.map-%{ver_rel}
%dir /lib/modules/%{ver_rel}
%dir /lib/modules/%{ver_rel}/kernel
/lib/modules/%{ver_rel}/kernel/arch
/lib/modules/%{ver_rel}/kernel/block
/lib/modules/%{ver_rel}/kernel/crypto
/lib/modules/%{ver_rel}/kernel/drivers
/lib/modules/%{ver_rel}/kernel/fs
/lib/modules/%{ver_rel}/kernel/kernel
/lib/modules/%{ver_rel}/kernel/lib
/lib/modules/%{ver_rel}/kernel/net
%exclude /lib/modules/%{ver_rel}/kernel/net/netfilter
%exclude /lib/modules/%{ver_rel}/kernel/net/*/netfilter
/lib/modules/%{ver_rel}/kernel/security
%dir /lib/modules/%{ver_rel}/misc
%exclude /lib/modules/%{ver_rel}/kernel/drivers/pcmcia
%exclude /lib/modules/%{ver_rel}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{ver_rel}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{ver_rel}/kernel/drivers/usb/host/sl811_cs.ko*
/lib/modules/%{ver_rel}/build
%ghost /lib/modules/%{ver_rel}/modules.*
%dir %{_sysconfdir}/modprobe.d/%{ver_rel}

%files libs
%defattr(644,root,root,755)
%dir /boot/libs-%{ver_rel}
%attr(755,root,root) /boot/libs-%{ver_rel}/addnote
/boot/libs-%{ver_rel}/*.o
/boot/libs-%{ver_rel}/zImage.lds

%files vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{ver_rel}

%files net-netfilter
%defattr(644,root,root,755)
/lib/modules/%{ver_rel}/kernel/net/netfilter
/lib/modules/%{ver_rel}/kernel/net/*/netfilter

%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{ver_rel}/kernel/drivers/pcmcia
/lib/modules/%{ver_rel}/kernel/drivers/*/pcmcia
/lib/modules/%{ver_rel}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{ver_rel}/kernel/drivers/telephony/ixj_pcmcia.ko*
/lib/modules/%{ver_rel}/kernel/drivers/usb/host/sl811_cs.ko*

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{ver}
%{_prefix}/src/linux-%{ver}/include
%{_prefix}/src/linux-%{ver}/config-up
%{_prefix}/src/linux-%{ver}/Module.symvers-up

%files module-build -f aux_files
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{ver}/Kbuild
%{_prefix}/src/linux-%{ver}/localversion
%{_prefix}/src/linux-%{ver}/arch/*/kernel/asm-offsets.*
%{_prefix}/src/linux-%{ver}/arch/*/kernel/sigframe.h
%dir %{_prefix}/src/linux-%{ver}/scripts
%dir %{_prefix}/src/linux-%{ver}/scripts/kconfig
%{_prefix}/src/linux-%{ver}/scripts/Kbuild.include
%{_prefix}/src/linux-%{ver}/scripts/Makefile*
%{_prefix}/src/linux-%{ver}/scripts/basic
%{_prefix}/src/linux-%{ver}/scripts/mkmakefile
%{_prefix}/src/linux-%{ver}/scripts/mod
%{_prefix}/src/linux-%{ver}/scripts/setlocalversion
%{_prefix}/src/linux-%{ver}/scripts/*.c
%{_prefix}/src/linux-%{ver}/scripts/*.sh
%{_prefix}/src/linux-%{ver}/scripts/kconfig/*

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{ver}/Documentation

%files source -f aux_files_exc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{ver}/arch/*/[!Mk]*
%{_prefix}/src/linux-%{ver}/arch/*/kernel/[!M]*
%exclude %{_prefix}/src/linux-%{ver}/arch/*/kernel/asm-offsets.*
%exclude %{_prefix}/src/linux-%{ver}/arch/*/kernel/sigframe.h
%{_prefix}/src/linux-%{ver}/block
%{_prefix}/src/linux-%{ver}/crypto
%{_prefix}/src/linux-%{ver}/drivers
%{_prefix}/src/linux-%{ver}/fs
%if %{with grsec_minimal}
%{_prefix}/src/linux-%{ver}/grsecurity
%endif
%{_prefix}/src/linux-%{ver}/init
%{_prefix}/src/linux-%{ver}/ipc
%{_prefix}/src/linux-%{ver}/kernel
%{_prefix}/src/linux-%{ver}/lib
%{_prefix}/src/linux-%{ver}/mm
%{_prefix}/src/linux-%{ver}/net
%{_prefix}/src/linux-%{ver}/scripts/*
%exclude %{_prefix}/src/linux-%{ver}/scripts/Kbuild.include
%exclude %{_prefix}/src/linux-%{ver}/scripts/Makefile*
%exclude %{_prefix}/src/linux-%{ver}/scripts/basic
%exclude %{_prefix}/src/linux-%{ver}/scripts/kconfig
%exclude %{_prefix}/src/linux-%{ver}/scripts/mkmakefile
%exclude %{_prefix}/src/linux-%{ver}/scripts/mod
%exclude %{_prefix}/src/linux-%{ver}/scripts/setlocalversion
%exclude %{_prefix}/src/linux-%{ver}/scripts/*.c
%exclude %{_prefix}/src/linux-%{ver}/scripts/*.sh
%{_prefix}/src/linux-%{ver}/sound
%{_prefix}/src/linux-%{ver}/security
%{_prefix}/src/linux-%{ver}/usr
%{_prefix}/src/linux-%{ver}/COPYING
%{_prefix}/src/linux-%{ver}/CREDITS
%{_prefix}/src/linux-%{ver}/MAINTAINERS
%{_prefix}/src/linux-%{ver}/README
%{_prefix}/src/linux-%{ver}/REPORTING-BUGS
