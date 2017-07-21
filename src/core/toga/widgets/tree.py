from .base import Widget


class Tree(Widget):
    '''
    Tree widget
    '''
    def __init__(self, headings, id=None, style=None, factory=None):
        '''
        Instantiate a new instance of the tree widget

        :param headings: The list of headings for the tree
        :type  headings: ``list`` of ``str``

        :param id:          An identifier for this widget.
        :type  id:          ``str``

        :param style:       an optional style object. If no style is provided then a
                            new one will be created for the widget.
        :type style:        :class:`colosseum.CSSNode`
        '''
        super().__init__(id=id, style=style, factory=factory)

        self.headings = headings
        self._impl = self.factory.Tree(interface=self)


