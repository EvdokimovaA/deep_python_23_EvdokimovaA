import unittest
from unittest import mock
from predict_message import SomeModel, predict_message_mood


class TestPredictMessage(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_bad_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model), 'неуд')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_good_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.9

            self.assertEqual(predict_message_mood('message', self.model), 'отл')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.5

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood_with_correct_thresholds(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model, 0.1, 0.5), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood_with_incorrect_thresholds(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.5

            def call_predict_message_mood():
                predict_message_mood('message', self.model, 0.8, 0.3)

            self.assertRaises(ValueError, call_predict_message_mood)

    def test_bad_thresholds(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.3

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_good_thresholds(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.8

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_near_edge_case_normal_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.30001
            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

            mock_model.return_value = 0.79999
            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_near_edge_case_bad_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.29999
            self.assertEqual(predict_message_mood('message', self.model), 'неуд')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_near_edge_case_good_mood(self):
        with mock.patch('predict_message.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.80001
            self.assertEqual(predict_message_mood('message', self.model), 'отл')
            self.assertEqual(mock_model.call_args.args, ('message',))
