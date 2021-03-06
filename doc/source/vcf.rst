*****************
Working With VCFs
*****************

The VCF Class
=============

panVCF.VCF(file)
    parameters:
        file - The VCF file which you want to load into panVCF

Data
----
    VCF.vcf
        Pandas dataframe of vcf data, excluding headers

    VCF.geno
        Pandas dataframe of genotype data

    VCF.head()
        Returns the headers for the vcf

Hardy-Weinberg
--------------
    `VCF.hardyweinberg(snp, excludeNan=True) <https://pyseq.readthedocs.org/en/latest/genotype.html#hardy-weinberg>`_

Changing Reference Genome
-------------------------
    VCF.change_base(old_reference_file, new_reference_file, chrom)
        Used when the reference genome of a vcf file must be changed. Must be done one chromosome at a time (vcf can have more than one, but the fasta files can only have one).
        
        parameters:
            old_reference_file - The fasta file that contains the data for the chromosome of interest that serves as the reference for the current vcf

            new_reference_file - The fasta file that contains the data for the chromosome of interest that is the desired reference for the vcf

            chrom - The chromosome of interest. For example '22' or 'Y'

        output:
            VCF - a new vcf object with a new VCF.vcf and VCF.geno

Indels
------
    isindel(line)
        parameters:
            line - the line of data to analyze
        output:
            Boolean - True if line is an indel, if not, False
