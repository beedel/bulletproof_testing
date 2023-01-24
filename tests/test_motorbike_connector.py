import unittest
from unittest.mock import patch, call
from src.Motorbike.MotorBikeConnector import MotorBikeConnector


class TestMotorBikeConnector(unittest.TestCase):

    @patch('src.Motorbike.Internet.frequests.post')
    def test_check_if_bike_exists(self, mock_post):
        # Arrange
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = "True"

        # Act
        connector = MotorBikeConnector()
        result = connector.check_if_bike_exists("Harley Davidson")

        # Assert
        mock_post.assert_called_with(url="www.bikernet.com/checkExist", json={'bikeName': "Harley Davidson"})

        # Assert
        self.assertEqual("True", result)

    @patch('src.Motorbike.Internet.frequests.post')
    @patch('builtins.print')
    def test_check_if_bike_exists_returns_404(self, mock_print, mock_post):
        # Arrange
        mock_post.return_value.status_code = 404
        mock_post.return_value.text = "Page not found"

        # Act
        connector = MotorBikeConnector()
        result = connector.check_if_bike_exists("Harley Davidson")

        # Assert mock called
        mock_post.assert_called_with(url="www.bikernet.com/checkExist", json={'bikeName': "Harley Davidson"})

        # Assert mock returned right calls
        self.assertEqual(result, None)
        mock_print.assert_has_calls([
            call("I got a not OK response"),
            call("Ooops something went wrong"),
        ], any_order=False)

    @patch('src.Motorbike.Internet.frequests.post')
    @patch('builtins.print')
    def test_check_if_bike_exists_with_exception(self, mock_print, mock_post):
        # Arrange
        mock_post.side_effect = Exception

        # Act
        connector = MotorBikeConnector()
        result = connector.check_if_bike_exists("Harley Davidson")

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_called_with("Ooops something went wrong")

    @patch('src.Motorbike.Internet.frequests.post')
    def test_get_price_for_bike(self, mock_post):
        # Arrange
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = "£6000"

        # Act
        connector = MotorBikeConnector()
        result = connector.get_price_for_bike("Harley Davidson")

        # Assert
        mock_post.assert_called_with(url="www.bikernet.com/getPriceForBike", json={'bikeName': "Harley Davidson"})

        # Assert
        self.assertEqual(result, "£6000")

    @patch('src.Motorbike.Internet.frequests.post')
    @patch('builtins.print')
    def test_get_price_for_bike_gives_404(self, mock_print, mock_post):
        # Arrange
        mock_post.return_value.status_code = 404
        mock_post.return_value.text = "Page not found"

        # Act
        connector = MotorBikeConnector()
        result = connector.get_price_for_bike("Harley Davidson")

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_has_calls([
            call("I got a not OK response"),
            call("Ooops something went wrong"),
        ], any_order=False)

    @patch('src.Motorbike.Internet.frequests.post')
    @patch('builtins.print')
    def test_get_price_for_bike_raises_exception(self, mock_print, mock_post):
        # Arrange
        mock_post.side_effect = Exception

        # Act
        connector = MotorBikeConnector()
        result = connector.get_price_for_bike("Harley Davidson")

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_called_with("Ooops something went wrong")


if __name__ == '__main__':
    unittest.main()
