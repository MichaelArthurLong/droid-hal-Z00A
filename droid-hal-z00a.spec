# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define rpm_device z00a
%define device Z00A
%define vendor asus

%define vendor_pretty ASUS
%define device_pretty Zenfone 2

%define device_target_cpu i486

%define installable_zip 1

%define straggler_files \
	/config_init.sh \
	/init.class_main.sh \
	/intel_prop.cfg \
	/rfkill_bt.sh \
	/selinux_version \
	/service_contexts \
	%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"
