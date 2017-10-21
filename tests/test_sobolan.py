import testtools
import mock

from animale import sobolan


class SobolanTests(testtools.TestCase):

    def setUp(self):
        super(SobolanTests, self).setUp()

        # initialize your stuffs.
        self.shobo = sobolan.Sobolan('gigi')

    def _delete_files(self):
        pass

    def test_multiply_sobolan(self):
        alt_shobo = sobolan.Sobolan('petrolieru')

        new_shobolan = self.shobo * alt_shobo

        self.assertEqual('gilieru', new_shobolan._name)

    @mock.patch.object(sobolan.random, 'randint')
    def test_produ_numere_random(self, mock_randint):
        mock_randint.return_value = 3

        random_number = self.shobo.produ_numere_random()

        self.assertEqual(3, random_number)
        mock_randint.assert_called_once_with(0, 10)
