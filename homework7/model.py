import datetime
import json


class TodoModel:
    id = 0
    message = ''
    create_time = ''
    update_time = ''
    status = '未完成'

    @classmethod
    def _load_data(cls) -> list:
        with open('database.json', 'r') as f:
            text = '\n'.join(f.readlines())
        return json.loads(text)

    @classmethod
    def _save_data(cls, data_list: list):
        with open('database.json', 'w') as f:
            f.write(json.dumps(data_list, ensure_ascii=False, default=lambda o: o.__dict__, indent=4))

    @classmethod
    def all(cls):
        ret = []
        data_list = cls._load_data()
        for data in data_list:  # type dict
            m = cls()
            for k, v in data.items():
                if hasattr(m, k):
                    setattr(m, k, v)
            ret.append(m)
        return ret

    @classmethod
    def add(cls, todo: dict):
        data = cls._load_data()

        m = cls()
        for k, v in todo.items():
            if hasattr(m, k):
                setattr(m, k, v)

        m.id = len(data)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        m.create_time = now
        m.update_time = now
        m.status = '未完成'

        data.append(m)
        cls._save_data(data)

    @classmethod
    def delete(cls, todo_id):
        # todo 自行实现
        ret = []
        data = cls._load_data()
        for m in data:
            if m['id'] != todo_id:
                ret.append(m)
        cls._save_data(ret)
        return ret

