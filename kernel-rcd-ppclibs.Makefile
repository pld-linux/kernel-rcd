
DEST = $(if $(DESTDIR),$(DESTDIR),unspecified)

INSTALL = install -D
MKDIR = install -d

# libraries
to_inst += crt0.o
to_inst += string.o
to_inst += prom.o
to_inst += stdio.o
to_inst += main.o
to_inst += div64.o
to_inst += infblock.o
to_inst += infcodes.o
to_inst += inffast.o
to_inst += inflate.o
to_inst += inftrees.o
to_inst += infutil.o

# empty elf
to_inst += kernel-vmlinux.strip.o

# ls script
to_inst += zImage.lds

# utils
to_inst += addnote


all: $(addprefix arch/powerpc/boot/,$(to_inst))


$(DESTDIR)/%: arch/powerpc/boot/% $(DEST)
	$(INSTALL) $< $@

install: all \
	$(addprefix $(DESTDIR)/,$(to_inst))
	
$(DESTDIR):
	$(MKDIR) $@

unspecified:
	@echo "DESTDIR must be specified"
	@exit 10

#vim:syntax=make
