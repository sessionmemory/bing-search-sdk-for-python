# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ResponseBase(msrest.serialization.Model):
    """Response base.

    :param type:
    :type type: str
    """

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResponseBase, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)


class Identifiable(ResponseBase):
    """Defines the identity of a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Identifiable, self).__init__(**kwargs)
        self.id = None


class Response(Identifiable):
    """Defines a response. All schemas that could be returned at the root of a response should inherit from this.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Response, self).__init__(**kwargs)
        self.read_link = None
        self.web_search_url = None


class Answer(Response):
    """Defines an answer.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Answer, self).__init__(**kwargs)


class Thing(Response):
    """Defines a thing.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image: ~custom_image_search_client.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Thing, self).__init__(**kwargs)
        self.name = None
        self.url = None
        self.image = None
        self.description = None
        self.alternate_name = None
        self.bing_id = None


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies, photographs, software programs, etc.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image: ~custom_image_search_client.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_image_search_client.models.Thing]
    :ivar text: Text content of this creative work.
    :vartype text: str
    """

    _validation = {
        'id': {'readonly': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreativeWork, self).__init__(**kwargs)
        self.thumbnail_url = None
        self.provider = None
        self.text = None


class Error(msrest.serialization.Model):
    """Defines the error that occurred.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code that identifies the category of error. Possible values
     include: "None", "ServerError", "InvalidRequest", "RateLimitExceeded", "InvalidAuthorization",
     "InsufficientAuthorization". Default value: "None".
    :type code: str or ~custom_image_search_client.models.ErrorCode
    :ivar sub_code: The error code that further helps to identify the error. Possible values
     include: "UnexpectedError", "ResourceError", "NotImplemented", "ParameterMissing",
     "ParameterInvalidValue", "HttpNotAllowed", "Blocked", "AuthorizationMissing",
     "AuthorizationRedundancy", "AuthorizationDisabled", "AuthorizationExpired".
    :vartype sub_code: str or ~custom_image_search_client.models.ErrorSubCode
    :param message: Required. A description of the error.
    :type message: str
    :ivar more_details: A description that provides additional information about the error.
    :vartype more_details: str
    :ivar parameter: The parameter in the request that caused the error.
    :vartype parameter: str
    :ivar value: The parameter's value in the request that was not valid.
    :vartype value: str
    """

    _validation = {
        'code': {'required': True},
        'sub_code': {'readonly': True},
        'message': {'required': True},
        'more_details': {'readonly': True},
        'parameter': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'sub_code': {'key': 'subCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'more_details': {'key': 'moreDetails', 'type': 'str'},
        'parameter': {'key': 'parameter', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', "None")
        self.sub_code = None
        self.message = kwargs['message']
        self.more_details = None
        self.parameter = None
        self.value = None


class ErrorResponse(Response):
    """The top-level response that represents a failed request.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :param errors: Required. A list of errors that describe the reasons why the request failed.
    :type errors: list[~custom_image_search_client.models.Error]
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'errors': {'required': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[Error]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.errors = kwargs['errors']


class MediaObject(CreativeWork):
    """Defines a media object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image: ~custom_image_search_client.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_image_search_client.models.Thing]
    :ivar text: Text content of this creative work.
    :vartype text: str
    :ivar content_url: Original URL to retrieve the source (file) for the media object (e.g the
     source URL for the image).
    :vartype content_url: str
    :ivar host_page_url: URL of the page that hosts the media object.
    :vartype host_page_url: str
    :ivar content_size: Size of the media object content (use format "value unit" e.g "1024 B").
    :vartype content_size: str
    :ivar encoding_format: Encoding format (e.g mp3, mp4, jpeg, etc).
    :vartype encoding_format: str
    :ivar host_page_display_url: Display URL of the page that hosts the media object.
    :vartype host_page_display_url: str
    :ivar width: The width of the media object, in pixels.
    :vartype width: int
    :ivar height: The height of the media object, in pixels.
    :vartype height: int
    """

    _validation = {
        'id': {'readonly': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
        'content_url': {'readonly': True},
        'host_page_url': {'readonly': True},
        'content_size': {'readonly': True},
        'encoding_format': {'readonly': True},
        'host_page_display_url': {'readonly': True},
        'width': {'readonly': True},
        'height': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'host_page_url': {'key': 'hostPageUrl', 'type': 'str'},
        'content_size': {'key': 'contentSize', 'type': 'str'},
        'encoding_format': {'key': 'encodingFormat', 'type': 'str'},
        'host_page_display_url': {'key': 'hostPageDisplayUrl', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MediaObject, self).__init__(**kwargs)
        self.content_url = None
        self.host_page_url = None
        self.content_size = None
        self.encoding_format = None
        self.host_page_display_url = None
        self.width = None
        self.height = None


class ImageObject(MediaObject):
    """Defines an image.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image: ~custom_image_search_client.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_image_search_client.models.Thing]
    :ivar text: Text content of this creative work.
    :vartype text: str
    :ivar content_url: Original URL to retrieve the source (file) for the media object (e.g the
     source URL for the image).
    :vartype content_url: str
    :ivar host_page_url: URL of the page that hosts the media object.
    :vartype host_page_url: str
    :ivar content_size: Size of the media object content (use format "value unit" e.g "1024 B").
    :vartype content_size: str
    :ivar encoding_format: Encoding format (e.g mp3, mp4, jpeg, etc).
    :vartype encoding_format: str
    :ivar host_page_display_url: Display URL of the page that hosts the media object.
    :vartype host_page_display_url: str
    :ivar width: The width of the media object, in pixels.
    :vartype width: int
    :ivar height: The height of the media object, in pixels.
    :vartype height: int
    :ivar thumbnail: The URL to a thumbnail of the image.
    :vartype thumbnail: ~custom_image_search_client.models.ImageObject
    :ivar image_insights_token: The token that you use in a subsequent call to the Image Search API
     to get additional information about the image. For information about using this token, see the
     insightsToken query parameter.
    :vartype image_insights_token: str
    :ivar image_id: Unique Id for the image.
    :vartype image_id: str
    :ivar accent_color: A three-byte hexadecimal number that represents the color that dominates
     the image. Use the color as the temporary background in your client until the image is loaded.
    :vartype accent_color: str
    :ivar visual_words: Visual representation of the image. Used for getting more sizes.
    :vartype visual_words: str
    """

    _validation = {
        'id': {'readonly': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
        'content_url': {'readonly': True},
        'host_page_url': {'readonly': True},
        'content_size': {'readonly': True},
        'encoding_format': {'readonly': True},
        'host_page_display_url': {'readonly': True},
        'width': {'readonly': True},
        'height': {'readonly': True},
        'thumbnail': {'readonly': True},
        'image_insights_token': {'readonly': True},
        'image_id': {'readonly': True},
        'accent_color': {'readonly': True},
        'visual_words': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'host_page_url': {'key': 'hostPageUrl', 'type': 'str'},
        'content_size': {'key': 'contentSize', 'type': 'str'},
        'encoding_format': {'key': 'encodingFormat', 'type': 'str'},
        'host_page_display_url': {'key': 'hostPageDisplayUrl', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'thumbnail': {'key': 'thumbnail', 'type': 'ImageObject'},
        'image_insights_token': {'key': 'imageInsightsToken', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
        'accent_color': {'key': 'accentColor', 'type': 'str'},
        'visual_words': {'key': 'visualWords', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ImageObject, self).__init__(**kwargs)
        self.thumbnail = None
        self.image_insights_token = None
        self.image_id = None
        self.accent_color = None
        self.visual_words = None


class SearchResultsAnswer(Response):
    """Defines a search result answer.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar total_estimated_matches: The estimated number of webpages that are relevant to the query.
     Use this number along with the count and offset query parameters to page the results.
    :vartype total_estimated_matches: long
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SearchResultsAnswer, self).__init__(**kwargs)
        self.total_estimated_matches = None


class Images(SearchResultsAnswer):
    """Defines an image answer.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar total_estimated_matches: The estimated number of webpages that are relevant to the query.
     Use this number along with the count and offset query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar next_offset: Used as part of deduping. Tells client the next offset that client should
     use in the next pagination request.
    :vartype next_offset: int
    :param value: Required. A list of image objects that are relevant to the query. If there are no
     results, the List is empty.
    :type value: list[~custom_image_search_client.models.ImageObject]
    """

    _validation = {
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'next_offset': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'next_offset': {'key': 'nextOffset', 'type': 'int'},
        'value': {'key': 'value', 'type': '[ImageObject]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Images, self).__init__(**kwargs)
        self.next_offset = None
        self.value = kwargs['value']


class Query(msrest.serialization.Model):
    """Defines a search query.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The query string. Use this string as the query term in a new search
     request.
    :type text: str
    :ivar display_text: The display version of the query term. This version of the query term may
     contain special characters that highlight the search term found in the query string. The string
     contains the highlighting characters only if the query enabled hit highlighting.
    :vartype display_text: str
    :ivar web_search_url: The URL that takes the user to the Bing search results page for the
     query.Only related search results include this field.
    :vartype web_search_url: str
    :ivar search_link: The URL that you use to get the results of the related search. Before using
     the URL, you must append query parameters as appropriate and include the Ocp-Apim-Subscription-
     Key header. Use this URL if you're displaying the results in your own user interface.
     Otherwise, use the webSearchUrl URL.
    :vartype search_link: str
    :ivar thumbnail: The URL to a thumbnail of a related image.
    :vartype thumbnail: ~custom_image_search_client.models.ImageObject
    """

    _validation = {
        'text': {'required': True},
        'display_text': {'readonly': True},
        'web_search_url': {'readonly': True},
        'search_link': {'readonly': True},
        'thumbnail': {'readonly': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'search_link': {'key': 'searchLink', 'type': 'str'},
        'thumbnail': {'key': 'thumbnail', 'type': 'ImageObject'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Query, self).__init__(**kwargs)
        self.text = kwargs['text']
        self.display_text = None
        self.web_search_url = None
        self.search_link = None
        self.thumbnail = None


class WebPage(CreativeWork):
    """Defines a webpage that is relevant to the query.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param type:
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image: ~custom_image_search_client.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_image_search_client.models.Thing]
    :ivar text: Text content of this creative work.
    :vartype text: str
    """

    _validation = {
        'id': {'readonly': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WebPage, self).__init__(**kwargs)