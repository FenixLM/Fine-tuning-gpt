from models.fine_tuning_model import FineTuningModel

class fineTuningController:
    def __init__(self):
        self.model = FineTuningModel

    def format_file(self):
        data = self.model.format_file()
        return data
    
    def charge_data(self):
        data = self.model().charge_data()
        print('id de nuestro dataset', data)
        return data
    
    def create_fine_tunig_job(self):
        data = self.model().create_fine_tunig_job()
        print('Data',data)
        return data

    def test_fine_tuning(self):
        data = self.model.test_fine_tuning()
        print('Respuesta del nuevo modelo',data)
        return data