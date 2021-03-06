import unittest, os

from genda.formats.panVCF import VCF

class TestLoadingVCF(unittest.TestCase):
    """ Testing loading VCF files into pandas
    """

    def setUp(self):
        self.filename = './data/chrY.test.vcf'
        self.VCF = VCF(self.filename)

    def testSamples(self):
        self.assertEqual(len(self.VCF.samples), 526)
        self.assertEqual(self.VCF.info[0][1],'1')
        self.assertEqual(self.VCF.gformat[0],'GT')
        self.assertEqual(self.VCF.novel[0],'Y_2649856_A')
        self.assertEqual('NA19088' in VCF.list_samples_with_alternate_allele(self.VCF,'rs11575897')
                , True)
        self.assertEqual(len(VCF.list_samples_with_alternate_allele(self.VCF,'rs11575897')),99)
        self.assertEqual(self.VCF.hardyweinberg('rs11575897'), False)

    def testInfo(self):
        pass



def main():
    unittest.main()

if __name__ == '__main__':
    print(__file__)
    main()


