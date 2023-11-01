import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # omat

    def test_negatiivinen_tilavuus_muuttuu_nollaksi(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_muuttuu_nollaksi(self):
        varasto = Varasto(10, -1)
        self.assertEqual(varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_maaraa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_liikaa_lisays_tayttaa_vain_ylarajaan(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)

    def test_negatiivinen_ottaminen_ei_muuta_maaraa(self):
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_liikaa_ottaminen_nollaa_maaran(self):
        self.varasto.lisaa_varastoon(1)
        self.varasto.ota_varastosta(2)
        self.assertEqual(self.varasto.saldo, 0)

    def test_saldo_ja_tila_tulostuvat_oikein(self):
        self.varasto.lisaa_varastoon(-2) # 0/10
        self.varasto.lisaa_varastoon(20) # 10/10
        self.varasto.lisaa_varastoon(4) # 10/10
        self.varasto.ota_varastosta(-1) # 10/10
        self.varasto.ota_varastosta(6) # 4/10
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
