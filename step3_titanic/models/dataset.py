from dataclasses import dataclass

@dataclass #데이터클래스로 해서 외부에서의 데이터 저장 가능하게 하는 것
class Dataset(object):
    context: str
    fname: str #파일네임
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter # setter = 외부에서 받은 값
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

