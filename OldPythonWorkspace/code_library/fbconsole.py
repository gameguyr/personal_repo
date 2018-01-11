  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>fbconsole/src/fbconsole.py at master · facebook/fbconsole · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="3jVwdgWzMKeIAP+rsihKF+lh8vQ8Axv9+fyjt/dCapg=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-93e28295e9de4310090c4fe2ed0851ddde77ddfa.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-2ef148486376675ad2c42348f04cbb83dcc5a10e.css" media="screen" rel="stylesheet" type="text/css" />
    
    


    <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-c86655d74d3a1c4761cfc641f9400895db04e2f8.js" type="text/javascript"></script>
    
    <script defer="defer" src="https://a248.e.akamai.net/assets.github.com/assets/github-9ba225d9e6c45ea1219dfb0a4bf829b03d47c271.js" type="text/javascript"></script>
    
    

      <link rel='permalink' href='/facebook/fbconsole/blob/8d66505c6c6a9689b29c677ddc81899ca19bb5ec/src/fbconsole.py'>
    <meta property="og:title" content="fbconsole"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/facebook/fbconsole"/>
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/gravatars/gravatar-140.png?1329275934"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="fbconsole - A micro api client for writing scripts against the Facebook Graph API."/>

    <meta name="description" content="fbconsole - A micro api client for writing scripts against the Facebook Graph API." />

  <link href="https://github.com/facebook/fbconsole/commits/master.atom" rel="alternate" title="Recent Commits to fbconsole:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production " data-blob-contribs-enabled="yes">
    <div id="wrapper">

    
    
    

      <div id="header" class="true clearfix">
        <div class="container clearfix">
          <a class="site-logo" href="https://github.com/">
            <!--[if IE]>
            <img alt="GitHub" class="github-logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7.png?1323882770" />
            <img alt="GitHub" class="github-logo-hover" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7-hover.png?1324325405" />
            <![endif]-->
            <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1337118069" />
            <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1337118069" />
          </a>


                  <!--
      make sure to use fully qualified URLs here since this nav
      is used on error pages on other domains
    -->
    <ul class="top-nav logged_out">
        <li class="pricing"><a href="https://github.com/plans">Signup and Pricing</a></li>
        <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
      <li class="features"><a href="https://github.com/features">Features</a></li>
        <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      <li class="login"><a href="https://github.com/login?return_to=%2Ffacebook%2Ffbconsole%2Fblob%2Fmaster%2Fsrc%2Ffbconsole.py">Sign in</a></li>
    </ul>



          
        </div>
      </div>

      

            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="container hentry">
        <div class="pagehead repohead instapaper_ignore readability-menu">
        <div class="title-actions-bar">
          



              <ul class="pagehead-actions">




          <li>
            <span class="watch-button"><a href="/login?return_to=%2Ffacebook%2Ffbconsole" class="minibutton btn-watch js-toggler-target entice tooltipped leftwards" title="You must be signed in to use this feature" rel="nofollow">Watch</a><a class="social-count js-social-count" href="/facebook/fbconsole/watchers">169</a></span>
          </li>
          <li>
            <a href="/login?return_to=%2Ffacebook%2Ffbconsole" class="minibutton btn-fork js-toggler-target fork-button entice tooltipped leftwards"  title="You must be signed in to use this feature" rel="nofollow">Fork</a><a href="/facebook/fbconsole/network" class="social-count">22</a>
          </li>

    </ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
            <span class="repo-label"><span>public</span></span>
            <span class="mega-icon mega-icon-public-repo"></span>
            <span class="author vcard">
<a href="/facebook" class="url fn" itemprop="url" rel="author">              <span itemprop="title">facebook</span>
              </a></span> /
            <strong><a href="/facebook/fbconsole" class="js-current-repository">fbconsole</a></strong>
          </h1>
        </div>

          

  <ul class="tabs">
    <li><a href="/facebook/fbconsole" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/facebook/fbconsole/network" highlight="repo_network">Network</a>
    <li><a href="/facebook/fbconsole/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>1</span></a></li>

      <li><a href="/facebook/fbconsole/issues" highlight="repo_issues">Issues <span class='counter'>5</span></a></li>


    <li><a href="/facebook/fbconsole/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>

  </ul>
 
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/facebook/fbconsole/tree-list/8d66505c6c6a9689b29c677ddc81899ca19bb5ec"
      data-blob-url-prefix="/facebook/fbconsole/blob/8d66505c6c6a9689b29c677ddc81899ca19bb5ec"
    >

  <div class="breadcrumb">
    <span class="bold"><a href="/facebook/fbconsole">fbconsole</a></span> /
    <input class="tree-finder-input js-navigation-enable" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/facebook/fbconsole/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever" rel="nofollow">Dismiss</a>
        <span class="bold">Octotip:</span> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list js-navigation-container">
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form accept-charset="UTF-8">
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        Go
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions subnav">
    <li><a href="/facebook/fbconsole/tags" class="" highlight="repo_tags">Tags <span class="counter">3</span></a></li>
    <li><a href="/facebook/fbconsole/downloads" class="blank downloads-blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
    
  </ul>

  <ul class="scope">
    <li class="switcher">

      <div class="context-menu-container js-menu-container js-context-menu">
        <a href="#"
           class="minibutton bigger switcher js-menu-target js-commitish-button btn-branch repo-tree"
           data-hotkey="w"
           data-master-branch="master"
           data-ref="master">
           <span><i>branch:</i> master</span>
        </a>

        <div class="context-pane commitish-context js-menu-content">
          <a href="javascript:;" class="close js-menu-close"><span class="mini-icon mini-icon-remove-close"></span></a>
          <div class="context-title">Switch branches/tags</div>
          <div class="context-body pane-selector commitish-selector js-navigation-container">
            <div class="filterbar">
              <input type="text" id="context-commitish-filter-field" class="js-navigation-enable" placeholder="Filter branches/tags" data-filterable />

              <ul class="tabs">
                <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
              </ul>
            </div>

            <div class="js-filter-tab js-filter-branches" data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              <div class="no-results js-not-filterable">Nothing to show</div>
                <div class="commitish-item branch-commitish selector-item js-navigation-item js-navigation-target selected">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/facebook/fbconsole/blob/master/src/fbconsole.py" class="js-navigation-open" data-name="master" rel="nofollow">master</a>
                  </h4>
                </div>
            </div>

            <div class="js-filter-tab js-filter-tags" style="display:none" data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              <div class="no-results js-not-filterable">Nothing to show</div>
                <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/facebook/fbconsole/blob/v0.3/src/fbconsole.py" class="js-navigation-open" data-name="v0.3" rel="nofollow">v0.3</a>
                  </h4>
                </div>
                <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/facebook/fbconsole/blob/v0.2/src/fbconsole.py" class="js-navigation-open" data-name="v0.2" rel="nofollow">v0.2</a>
                  </h4>
                </div>
                <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/facebook/fbconsole/blob/v0.1/src/fbconsole.py" class="js-navigation-open" data-name="v0.1" rel="nofollow">v0.1</a>
                  </h4>
                </div>
            </div>
          </div>
        </div><!-- /.commitish-context-context -->
      </div>

    </li>
  </ul>

  <ul class="subnav with-scope">

    <li><a href="/facebook/fbconsole" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/facebook/fbconsole/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/facebook/fbconsole/branches" class="" highlight="repo_branches" rel="nofollow">Branches <span class="counter">1</span></a></li>
  </ul>

</div>

  
  
  


          

        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" data-pjax-container>
          





<!-- block_view_fragment_key: views10/v8/blob:v21:05cf9ac0bf833086857e7d0826108b7f -->
  <div id="slider">

    <div class="breadcrumb" data-path="src/fbconsole.py/">
      <b itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/facebook/fbconsole/tree/8d66505c6c6a9689b29c677ddc81899ca19bb5ec" class="js-rewrite-sha" itemprop="url"><span itemprop="title">fbconsole</span></a></b> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/facebook/fbconsole/tree/8d66505c6c6a9689b29c677ddc81899ca19bb5ec/src" class="js-rewrite-sha" itemscope="url"><span itemprop="title">src</span></a></span> / <strong class="final-path">fbconsole.py</strong> <span class="js-clippy mini-icon mini-icon-clippy " data-clipboard-text="src/fbconsole.py" data-copied-hint="copied!" data-copy-hint="copy to clipboard"></span>
    </div>


      <div class="commit file-history-tease" data-path="src/fbconsole.py/">
        <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/7216e50c65e8f5a9f4cf33ebb89c6221?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
        <span class="author"><a href="/pcardune">pcardune</a></span>
        <time class="js-relative-date" datetime="2012-03-24T20:44:07-07:00" title="2012-03-24 20:44:07">March 24, 2012</time>
        <div class="commit-title">
            <a href="/facebook/fbconsole/commit/8d66505c6c6a9689b29c677ddc81899ca19bb5ec" class="message">- fix a bug with python3.2 support</a>
        </div>

        <div class="participation">
          <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
          
        </div>
        <div id="blob_contributors_box" style="display:none">
          <h2>Users on GitHub who have contributed to this file</h2>
          <ul class="facebox-user-list">
            <li>
              <img height="24" src="https://secure.gravatar.com/avatar/7216e50c65e8f5a9f4cf33ebb89c6221?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
              <a href="/pcardune">pcardune</a>
            </li>
          </ul>
        </div>
      </div>

    <div class="frames">
      <div class="frame frame-center" data-path="src/fbconsole.py/" data-permalink-url="/facebook/fbconsole/blob/8d66505c6c6a9689b29c677ddc81899ca19bb5ec/src/fbconsole.py" data-title="fbconsole/src/fbconsole.py at master · facebook/fbconsole · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">100644</span>
                  <span>713 lines (587 sloc)</span>
                <span>24.241 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                    <a class="grouped-button file-edit-link minibutton bigger lighter js-rewrite-sha" href="/facebook/fbconsole/edit/8d66505c6c6a9689b29c677ddc81899ca19bb5ec/src/fbconsole.py" data-method="post" rel="nofollow" data-hotkey="e">Edit this file</a>
                  </li>

                <li>
                  <a href="/facebook/fbconsole/raw/master/src/fbconsole.py" class="minibutton btn-raw grouped-button bigger lighter" id="raw-url"><span class="icon"></span>Raw</a>
                </li>
                  <li>
                    <a href="/facebook/fbconsole/blame/master/src/fbconsole.py" class="minibutton btn-blame grouped-button bigger lighter"><span class="icon"></span>Blame</a>
                  </li>
                <li>
                  <a href="/facebook/fbconsole/commits/master/src/fbconsole.py" class="minibutton btn-history grouped-button bigger lighter" rel="nofollow"><span class="icon"></span>History</a>
                </li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
<span id="L635" rel="#L635">635</span>
<span id="L636" rel="#L636">636</span>
<span id="L637" rel="#L637">637</span>
<span id="L638" rel="#L638">638</span>
<span id="L639" rel="#L639">639</span>
<span id="L640" rel="#L640">640</span>
<span id="L641" rel="#L641">641</span>
<span id="L642" rel="#L642">642</span>
<span id="L643" rel="#L643">643</span>
<span id="L644" rel="#L644">644</span>
<span id="L645" rel="#L645">645</span>
<span id="L646" rel="#L646">646</span>
<span id="L647" rel="#L647">647</span>
<span id="L648" rel="#L648">648</span>
<span id="L649" rel="#L649">649</span>
<span id="L650" rel="#L650">650</span>
<span id="L651" rel="#L651">651</span>
<span id="L652" rel="#L652">652</span>
<span id="L653" rel="#L653">653</span>
<span id="L654" rel="#L654">654</span>
<span id="L655" rel="#L655">655</span>
<span id="L656" rel="#L656">656</span>
<span id="L657" rel="#L657">657</span>
<span id="L658" rel="#L658">658</span>
<span id="L659" rel="#L659">659</span>
<span id="L660" rel="#L660">660</span>
<span id="L661" rel="#L661">661</span>
<span id="L662" rel="#L662">662</span>
<span id="L663" rel="#L663">663</span>
<span id="L664" rel="#L664">664</span>
<span id="L665" rel="#L665">665</span>
<span id="L666" rel="#L666">666</span>
<span id="L667" rel="#L667">667</span>
<span id="L668" rel="#L668">668</span>
<span id="L669" rel="#L669">669</span>
<span id="L670" rel="#L670">670</span>
<span id="L671" rel="#L671">671</span>
<span id="L672" rel="#L672">672</span>
<span id="L673" rel="#L673">673</span>
<span id="L674" rel="#L674">674</span>
<span id="L675" rel="#L675">675</span>
<span id="L676" rel="#L676">676</span>
<span id="L677" rel="#L677">677</span>
<span id="L678" rel="#L678">678</span>
<span id="L679" rel="#L679">679</span>
<span id="L680" rel="#L680">680</span>
<span id="L681" rel="#L681">681</span>
<span id="L682" rel="#L682">682</span>
<span id="L683" rel="#L683">683</span>
<span id="L684" rel="#L684">684</span>
<span id="L685" rel="#L685">685</span>
<span id="L686" rel="#L686">686</span>
<span id="L687" rel="#L687">687</span>
<span id="L688" rel="#L688">688</span>
<span id="L689" rel="#L689">689</span>
<span id="L690" rel="#L690">690</span>
<span id="L691" rel="#L691">691</span>
<span id="L692" rel="#L692">692</span>
<span id="L693" rel="#L693">693</span>
<span id="L694" rel="#L694">694</span>
<span id="L695" rel="#L695">695</span>
<span id="L696" rel="#L696">696</span>
<span id="L697" rel="#L697">697</span>
<span id="L698" rel="#L698">698</span>
<span id="L699" rel="#L699">699</span>
<span id="L700" rel="#L700">700</span>
<span id="L701" rel="#L701">701</span>
<span id="L702" rel="#L702">702</span>
<span id="L703" rel="#L703">703</span>
<span id="L704" rel="#L704">704</span>
<span id="L705" rel="#L705">705</span>
<span id="L706" rel="#L706">706</span>
<span id="L707" rel="#L707">707</span>
<span id="L708" rel="#L708">708</span>
<span id="L709" rel="#L709">709</span>
<span id="L710" rel="#L710">710</span>
<span id="L711" rel="#L711">711</span>
<span id="L712" rel="#L712">712</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c">#</span></div><div class='line' id='LC3'><span class="c"># Copyright 2010-present Facebook</span></div><div class='line' id='LC4'><span class="c">#</span></div><div class='line' id='LC5'><span class="c"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may</span></div><div class='line' id='LC6'><span class="c"># not use this file except in compliance with the License. You may obtain</span></div><div class='line' id='LC7'><span class="c"># a copy of the License at</span></div><div class='line' id='LC8'><span class="c">#</span></div><div class='line' id='LC9'><span class="c">#     http://www.apache.org/licenses/LICENSE-2.0</span></div><div class='line' id='LC10'><span class="c">#</span></div><div class='line' id='LC11'><span class="c"># Unless required by applicable law or agreed to in writing, software</span></div><div class='line' id='LC12'><span class="c"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT</span></div><div class='line' id='LC13'><span class="c"># WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the</span></div><div class='line' id='LC14'><span class="c"># License for the specific language governing permissions and limitations</span></div><div class='line' id='LC15'><span class="c"># under the License.</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="kn">import</span> <span class="nn">BaseHTTPServer</span></div><div class='line' id='LC18'><span class="kn">import</span> <span class="nn">cookielib</span></div><div class='line' id='LC19'><span class="kn">import</span> <span class="nn">httplib</span></div><div class='line' id='LC20'><span class="kn">import</span> <span class="nn">anyjson</span> <span class="kn">as</span> <span class="nn">json</span></div><div class='line' id='LC21'><span class="kn">import</span> <span class="nn">random</span></div><div class='line' id='LC22'><span class="kn">import</span> <span class="nn">mimetypes</span></div><div class='line' id='LC23'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC24'><span class="kn">import</span> <span class="nn">os.path</span></div><div class='line' id='LC25'><span class="kn">import</span> <span class="nn">stat</span></div><div class='line' id='LC26'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC27'><span class="kn">import</span> <span class="nn">types</span></div><div class='line' id='LC28'><span class="kn">import</span> <span class="nn">urllib</span></div><div class='line' id='LC29'><span class="kn">import</span> <span class="nn">webbrowser</span></div><div class='line' id='LC30'><span class="kn">import</span> <span class="nn">StringIO</span></div><div class='line' id='LC31'><span class="kn">import</span> <span class="nn">six</span></div><div class='line' id='LC32'><span class="kn">from</span> <span class="nn">six</span> <span class="kn">import</span> <span class="n">b</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><span class="n">poster_is_available</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC35'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># try to use poster if it is available</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">poster.streaminghttp</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">poster.encode</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">poster</span><span class="o">.</span><span class="n">streaminghttp</span><span class="o">.</span><span class="n">register_openers</span><span class="p">()</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">poster_is_available</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC41'><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span> <span class="c"># we can live without this.</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="kn">from</span> <span class="nn">urlparse</span> <span class="kn">import</span> <span class="n">urlparse</span></div><div class='line' id='LC45'><span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pprint</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urlparse</span> <span class="kn">import</span> <span class="n">parse_qs</span></div><div class='line' id='LC49'><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">cgi</span> <span class="kn">import</span> <span class="n">parse_qs</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'><span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">io</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FileType</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">IOBase</span></div><div class='line' id='LC55'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FileType</span> <span class="o">=</span> <span class="n">types</span><span class="o">.</span><span class="n">FileType</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">build_opener</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">HTTPCookieProcessor</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">BaseHandler</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">HTTPHandler</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">urlopen</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">Request</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.parse</span> <span class="kn">import</span> <span class="n">urlencode</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.error</span> <span class="kn">import</span> <span class="n">HTTPError</span></div><div class='line' id='LC67'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">build_opener</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">HTTPCookieProcessor</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">BaseHandler</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">HTTPHandler</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">urlopen</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">HTTPError</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">Request</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib</span> <span class="kn">import</span> <span class="n">urlencode</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><span class="n">APP_ID</span> <span class="o">=</span> <span class="s">&#39;179745182062082&#39;</span></div><div class='line' id='LC78'><span class="n">SERVER_PORT</span> <span class="o">=</span> <span class="mi">8080</span></div><div class='line' id='LC79'><span class="n">ACCESS_TOKEN</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC80'><span class="n">CLIENT</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC81'><span class="n">ACCESS_TOKEN_FILE</span> <span class="o">=</span> <span class="s">&#39;.fb_access_token&#39;</span></div><div class='line' id='LC82'><span class="n">AUTH_SCOPE</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC83'><span class="n">BATCH_REQUEST_LIMIT</span> <span class="o">=</span> <span class="mi">50</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'><span class="n">AUTH_SUCCESS_HTML</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC86'><span class="s">You have successfully logged in to facebook with fbconsole.</span></div><div class='line' id='LC87'><span class="s">You can close this window now.</span></div><div class='line' id='LC88'><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;help&#39;</span><span class="p">,</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;authenticate&#39;</span><span class="p">,</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;logout&#39;</span><span class="p">,</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;graph_url&#39;</span><span class="p">,</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;oauth_url&#39;</span><span class="p">,</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;Batch&#39;</span><span class="p">,</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get&#39;</span><span class="p">,</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;post&#39;</span><span class="p">,</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;delete&#39;</span><span class="p">,</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;shell&#39;</span><span class="p">,</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;fql&#39;</span><span class="p">,</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;iter_pages&#39;</span><span class="p">,</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;Client&#39;</span><span class="p">,</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;APP_ID&#39;</span><span class="p">,</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;SERVER_PORT&#39;</span><span class="p">,</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ACCESS_TOKEN&#39;</span><span class="p">,</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;AUTH_SCOPE&#39;</span><span class="p">,</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ACCESS_TOKEN_FILE&#39;</span><span class="p">]</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'><span class="k">class</span> <span class="nc">_MultipartPostHandler</span><span class="p">(</span><span class="n">BaseHandler</span><span class="p">):</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">handler_order</span> <span class="o">=</span> <span class="n">HTTPHandler</span><span class="o">.</span><span class="n">handler_order</span> <span class="o">-</span> <span class="mi">10</span> <span class="c"># needs to run first</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">http_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">get_data</span><span class="p">()</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">types</span><span class="o">.</span><span class="n">StringTypes</span><span class="p">):</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">FileType</span><span class="p">):</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;not a valid non-string sequence or mapping object&quot;</span><span class="p">)</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">files</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">urlencode</span><span class="p">(</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">)</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">boundary</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">multipart_encode</span><span class="p">(</span><span class="n">params</span><span class="p">,</span> <span class="n">files</span><span class="p">)</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">contenttype</span> <span class="o">=</span> <span class="s">&#39;multipart/form-data; boundary=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request</span><span class="o">.</span><span class="n">add_unredirected_header</span><span class="p">(</span><span class="s">&#39;Content-Type&#39;</span><span class="p">,</span> <span class="n">contenttype</span><span class="p">)</span></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request</span><span class="o">.</span><span class="n">add_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">request</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">https_request</span> <span class="o">=</span> <span class="n">http_request</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">multipart_encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">,</span> <span class="n">files</span><span class="p">,</span> <span class="n">boundary</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="nb">buffer</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">boundary</span> <span class="o">=</span> <span class="n">boundary</span> <span class="ow">or</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;--------------------</span><span class="si">%s</span><span class="s">---&#39;</span> <span class="o">%</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">())</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">=</span> <span class="nb">buffer</span> <span class="ow">or</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">params</span><span class="p">:</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;--</span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span><span class="p">)</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;Content-Disposition: form-data; name=&quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="n">key</span><span class="p">)</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n\r\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">value</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">fd</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">file_size</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">fstat</span><span class="p">(</span><span class="n">fd</span><span class="o">.</span><span class="n">fileno</span><span class="p">())[</span><span class="n">stat</span><span class="o">.</span><span class="n">ST_SIZE</span><span class="p">]</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">fd</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">contenttype</span> <span class="o">=</span> <span class="n">mimetypes</span><span class="o">.</span><span class="n">guess_type</span><span class="p">(</span><span class="n">filename</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">or</span> <span class="s">&#39;application/octet-stream&#39;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;--</span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;Content-Disposition: form-data; &#39;</span><span class="p">)</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;name=&quot;</span><span class="si">%s</span><span class="s">&quot;; filename=&quot;</span><span class="si">%s</span><span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">filename</span><span class="p">))</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;Content-Type: </span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">contenttype</span><span class="p">)</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fd</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">fd</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> <span class="o">+</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="n">b</span><span class="p">(</span><span class="s">&#39;--</span><span class="si">%s</span><span class="s">--</span><span class="se">\r\n\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span><span class="p">)</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">boundary</span> <span class="o">=</span> <span class="n">boundary</span> <span class="ow">or</span> <span class="s">&#39;--------------------</span><span class="si">%s</span><span class="s">---&#39;</span> <span class="o">%</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">=</span> <span class="nb">buffer</span> <span class="ow">or</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">params</span><span class="p">:</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;--</span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;Content-Disposition: form-data; name=&quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="n">key</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\r\n\r\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">value</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">fd</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">file_size</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">fstat</span><span class="p">(</span><span class="n">fd</span><span class="o">.</span><span class="n">fileno</span><span class="p">())[</span><span class="n">stat</span><span class="o">.</span><span class="n">ST_SIZE</span><span class="p">]</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">fd</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">contenttype</span> <span class="o">=</span> <span class="n">mimetypes</span><span class="o">.</span><span class="n">guess_type</span><span class="p">(</span><span class="n">filename</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">or</span> <span class="s">&#39;application/octet-stream&#39;</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;--</span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;Content-Disposition: form-data; &#39;</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;name=&quot;</span><span class="si">%s</span><span class="s">&quot;; filename=&quot;</span><span class="si">%s</span><span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;Content-Type: </span><span class="si">%s</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">contenttype</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fd</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">fd</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">+=</span> <span class="s">&#39;--</span><span class="si">%s</span><span class="s">--</span><span class="se">\r\n\r\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">boundary</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">boundary</span><span class="p">,</span> <span class="nb">buffer</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'><span class="k">class</span> <span class="nc">_RequestHandler</span><span class="p">(</span><span class="n">BaseHTTPServer</span><span class="o">.</span><span class="n">BaseHTTPRequestHandler</span><span class="p">):</span></div><div class='line' id='LC183'><br/></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">do_GET</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">ACCESS_TOKEN</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">send_response</span><span class="p">(</span><span class="mi">200</span><span class="p">)</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">send_header</span><span class="p">(</span><span class="s">&quot;Content-type&quot;</span><span class="p">,</span> <span class="s">&quot;text/html&quot;</span><span class="p">)</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">end_headers</span><span class="p">()</span></div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="n">parse_qs</span><span class="p">(</span><span class="n">urlparse</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">query</span><span class="p">)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ACCESS_TOKEN</span> <span class="o">=</span> <span class="n">params</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;access_token&#39;</span><span class="p">,</span> <span class="p">[</span><span class="bp">None</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ACCESS_TOKEN</span><span class="p">:</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;scope&#39;</span><span class="p">:</span> <span class="n">AUTH_SCOPE</span><span class="p">,</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;access_token&#39;</span><span class="p">:</span> <span class="n">ACCESS_TOKEN</span><span class="p">}</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expiration</span> <span class="o">=</span> <span class="n">params</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;expires_in&#39;</span><span class="p">,</span> <span class="p">[</span><span class="bp">None</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">expiration</span><span class="p">:</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">expiration</span> <span class="o">==</span> <span class="s">&#39;0&#39;</span><span class="p">:</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this is what&#39;s returned when offline_access is requested</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="p">[</span><span class="s">&#39;expires_at&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;never&#39;</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="p">[</span><span class="s">&#39;expires_at&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span><span class="o">+</span><span class="nb">int</span><span class="p">(</span><span class="n">expiration</span><span class="p">))</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">open</span><span class="p">(</span><span class="n">ACCESS_TOKEN_FILE</span><span class="p">,</span><span class="s">&#39;w&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">))</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">b</span><span class="p">(</span><span class="n">AUTH_SUCCESS_HTML</span><span class="p">))</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">b</span><span class="p">(</span><span class="s">&#39;&lt;html&gt;&lt;head&gt;&#39;</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;&lt;script&gt;location = &quot;?&quot;+location.hash.slice(1);&lt;/script&gt;&#39;</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;&lt;/head&gt;&lt;/html&gt;&#39;</span><span class="p">))</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'><span class="k">class</span> <span class="nc">ApiException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC210'><br/></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="n">error_type</span><span class="p">,</span> <span class="n">code</span><span class="p">):</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">ApiException</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">message</span><span class="p">)</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">error_type</span> <span class="o">=</span> <span class="n">error_type</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">code</span> <span class="o">=</span> <span class="n">code</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@staticmethod</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="n">data</span><span class="p">):</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error_type</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;type&#39;</span><span class="p">)</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">subclass</span> <span class="ow">in</span> <span class="n">ApiException</span><span class="o">.</span><span class="n">__subclasses__</span><span class="p">():</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">subclass</span><span class="o">.</span><span class="n">__name__</span> <span class="o">==</span> <span class="n">error_type</span><span class="p">:</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">subclass</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;message&#39;</span><span class="p">),</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;error_type&#39;</span><span class="p">),</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;code&#39;</span><span class="p">))</span></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">UnknownApiException</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;message&#39;</span><span class="p">),</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;error_type&#39;</span><span class="p">),</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;code&#39;</span><span class="p">))</span></div><div class='line' id='LC228'><br/></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'><span class="k">class</span> <span class="nc">UnknownApiException</span><span class="p">(</span><span class="n">ApiException</span><span class="p">):</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Some unknown error.&quot;&quot;&quot;</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'><span class="k">class</span> <span class="nc">OAuthException</span><span class="p">(</span><span class="n">ApiException</span><span class="p">):</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Just an oath exception.&quot;&quot;&quot;</span></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'><br/></div><div class='line' id='LC237'><span class="k">def</span> <span class="nf">_handle_http_error</span><span class="p">(</span><span class="n">e</span><span class="p">):</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">body</span> <span class="o">=</span> <span class="n">e</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">body</span> <span class="o">=</span> <span class="n">body</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">)</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">body</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">body</span><span class="p">)</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error</span> <span class="o">=</span> <span class="n">body</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;error&#39;</span><span class="p">)</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">error</span><span class="p">:</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ApiException</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="n">error</span><span class="p">)</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">e</span></div><div class='line' id='LC250'><br/></div><div class='line' id='LC251'><span class="k">def</span> <span class="nf">_safe_url_load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Wrapper around urlopen that translates http errors into nicer exceptions.&quot;&quot;&quot;</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">urlopen</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">HTTPError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error</span> <span class="o">=</span> <span class="n">_handle_http_error</span><span class="p">(</span><span class="n">e</span><span class="p">)</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">error</span></div><div class='line' id='LC258'><br/></div><div class='line' id='LC259'><span class="k">def</span> <span class="nf">_safe_json_load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="n">_safe_url_load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">six</span><span class="o">.</span><span class="n">PY3</span><span class="p">:</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">))</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'><span class="k">def</span> <span class="nf">help</span><span class="p">():</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Print out some helpful information&quot;&quot;&quot;</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;&#39;&#39;</span></div><div class='line' id='LC269'><span class="s">The following commands are available:</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'><span class="s">help() - display this help message</span></div><div class='line' id='LC272'><span class="s">authenticate() - authenticate with facebook.</span></div><div class='line' id='LC273'><span class="s">logout() - Remove the cached access token, forcing authenticate() to get a new</span></div><div class='line' id='LC274'><span class="s">           access token</span></div><div class='line' id='LC275'><span class="s">graph_url(path, params) - get the full url to a graph api path</span></div><div class='line' id='LC276'><span class="s">get(path, params) - call the graph api with the given path and query parameters</span></div><div class='line' id='LC277'><span class="s">post(path, data) - post data to the graph api with the given path</span></div><div class='line' id='LC278'><span class="s">delete(path, params) - send a delete request</span></div><div class='line' id='LC279'><span class="s">fql(query) - make an fql request</span></div><div class='line' id='LC280'><span class="s">&#39;&#39;&#39;</span></div><div class='line' id='LC281'><br/></div><div class='line' id='LC282'><span class="k">def</span> <span class="nf">authenticate</span><span class="p">():</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Authenticate with facebook so you can make api calls that require auth.</span></div><div class='line' id='LC284'><br/></div><div class='line' id='LC285'><span class="sd">    Alternatively you can just set the ACCESS_TOKEN global variable in this</span></div><div class='line' id='LC286'><span class="sd">    module to set an access token you get from facebook.</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'><span class="sd">    If you want to request certain permissions, set the AUTH_SCOPE global</span></div><div class='line' id='LC289'><span class="sd">    variable to the list of permissions you want.</span></div><div class='line' id='LC290'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">ACCESS_TOKEN</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">needs_auth</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">ACCESS_TOKEN_FILE</span><span class="p">):</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="n">ACCESS_TOKEN_FILE</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expires_at</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;expires_at&#39;</span><span class="p">)</span></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">still_valid</span> <span class="o">=</span> <span class="n">expires_at</span> <span class="ow">and</span> <span class="p">(</span><span class="n">expires_at</span> <span class="o">==</span> <span class="s">&#39;never&#39;</span> <span class="ow">or</span> <span class="n">expires_at</span> <span class="o">&gt;</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">still_valid</span> <span class="ow">and</span> <span class="nb">set</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;scope&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">issuperset</span><span class="p">(</span><span class="n">AUTH_SCOPE</span><span class="p">):</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ACCESS_TOKEN</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&#39;access_token&#39;</span><span class="p">]</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">needs_auth</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC300'><br/></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">needs_auth</span><span class="p">:</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">webbrowser</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">oauth_url</span><span class="p">(</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">APP_ID</span><span class="p">,</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;http://127.0.0.1:</span><span class="si">%s</span><span class="s">/&#39;</span> <span class="o">%</span> <span class="n">SERVER_PORT</span><span class="p">,</span> <span class="n">AUTH_SCOPE</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">))</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">httpd</span> <span class="o">=</span> <span class="n">BaseHTTPServer</span><span class="o">.</span><span class="n">HTTPServer</span><span class="p">((</span><span class="s">&#39;127.0.0.1&#39;</span><span class="p">,</span> <span class="n">SERVER_PORT</span><span class="p">),</span> <span class="n">_RequestHandler</span><span class="p">)</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">ACCESS_TOKEN</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">httpd</span><span class="o">.</span><span class="n">handle_request</span><span class="p">()</span></div><div class='line' id='LC310'><br/></div><div class='line' id='LC311'><span class="k">def</span> <span class="nf">logout</span><span class="p">():</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Logout of facebook.  This just removes the cached access token.&quot;&quot;&quot;</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">ACCESS_TOKEN_FILE</span><span class="p">):</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">ACCESS_TOKEN_FILE</span><span class="p">)</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'><span class="k">class</span> <span class="nc">_GraphRequest</span><span class="p">:</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">ignore_result</span><span class="p">):</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">method</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">params</span> <span class="o">=</span> <span class="n">params</span> <span class="ow">or</span> <span class="p">{}</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">ignore_result</span> <span class="o">=</span> <span class="n">ignore_result</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">error</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC327'><br/></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_result</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">error</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span></div><div class='line' id='LC332'><br/></div><div class='line' id='LC333'><span class="k">class</span> <span class="nc">Batch</span><span class="p">:</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;A class that lets you batch multiple graph api calls into a single request.</span></div><div class='line' id='LC335'><br/></div><div class='line' id='LC336'><span class="sd">    First we create a new batch instance.</span></div><div class='line' id='LC337'><br/></div><div class='line' id='LC338'><span class="sd">      &gt;&gt;&gt; batch = Batch()</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'><span class="sd">    Then we can start fetching a bunch of stuff by calling</span></div><div class='line' id='LC341'><span class="sd">    get/post/delete/etc. on the batch object.  When calling these methods, a</span></div><div class='line' id='LC342'><span class="sd">    request object will be returned which can be used to fetch the result of</span></div><div class='line' id='LC343'><span class="sd">    that request after the batch has been sent.  By passing in a name, you can</span></div><div class='line' id='LC344'><span class="sd">    refer to the results of a previous request in a subsequent request using the</span></div><div class='line' id='LC345'><span class="sd">    special syntax defined documented here:</span></div><div class='line' id='LC346'><span class="sd">    https://developers.facebook.com/docs/reference/api/batch/</span></div><div class='line' id='LC347'><br/></div><div class='line' id='LC348'><span class="sd">      &gt;&gt;&gt; me = batch.get(&#39;/me&#39;, name=&#39;me&#39;)</span></div><div class='line' id='LC349'><span class="sd">      &gt;&gt;&gt; coke = batch.get(&#39;/cocacola&#39;, name=&#39;coke&#39;)</span></div><div class='line' id='LC350'><br/></div><div class='line' id='LC351'><span class="sd">    If you pass in ignore_result=True when making the request, then no request</span></div><div class='line' id='LC352'><span class="sd">    object will be returned and the results will not be passed down from</span></div><div class='line' id='LC353'><span class="sd">    facebook.  You can still use the results in other requests using the</span></div><div class='line' id='LC354'><span class="sd">    specialized syntax, but facebook won&#39;t send the results back.</span></div><div class='line' id='LC355'><br/></div><div class='line' id='LC356'><span class="sd">      &gt;&gt;&gt; image = open(&quot;icon.gif&quot;, &quot;rb&quot;)</span></div><div class='line' id='LC357'><span class="sd">      &gt;&gt;&gt; batch.post(&#39;/me/photos&#39;,</span></div><div class='line' id='LC358'><span class="sd">      ...            {&#39;name&#39;: &#39;{result=me:$.name} likes {result=coke:$.name}&#39;,</span></div><div class='line' id='LC359'><span class="sd">      ...             &#39;source&#39;: image},</span></div><div class='line' id='LC360'><span class="sd">      ...            name=&#39;photo&#39;,</span></div><div class='line' id='LC361'><span class="sd">      ...            ignore_result=True)</span></div><div class='line' id='LC362'><span class="sd">      &gt;&gt;&gt; photo = batch.get(&#39;/{result=photo:$.id}&#39;)</span></div><div class='line' id='LC363'><br/></div><div class='line' id='LC364'><span class="sd">    Now we can send the request:</span></div><div class='line' id='LC365'><br/></div><div class='line' id='LC366'><span class="sd">      &gt;&gt;&gt; batch.send()</span></div><div class='line' id='LC367'><span class="sd">      &gt;&gt;&gt; image.close()</span></div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'><span class="sd">    And look at the results:</span></div><div class='line' id='LC370'><br/></div><div class='line' id='LC371'><span class="sd">      &gt;&gt;&gt; print me.get_result()[&#39;name&#39;]</span></div><div class='line' id='LC372'><span class="sd">      David Amcafiaddddh Yangstein</span></div><div class='line' id='LC373'><br/></div><div class='line' id='LC374'><span class="sd">      &gt;&gt;&gt; print coke.get_result()[&#39;name&#39;]</span></div><div class='line' id='LC375'><span class="sd">      Coca-Cola</span></div><div class='line' id='LC376'><br/></div><div class='line' id='LC377'><span class="sd">      &gt;&gt;&gt; print photo.get_result()[&#39;name&#39;]</span></div><div class='line' id='LC378'><span class="sd">      David Amcafiaddddh Yangstein likes Coca-Cola</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'><span class="sd">    If you try to send a batch request twice, it will fail.  You must</span></div><div class='line' id='LC381'><span class="sd">    reconstruct a new batch.</span></div><div class='line' id='LC382'><br/></div><div class='line' id='LC383'><span class="sd">      &gt;&gt;&gt; batch.send()</span></div><div class='line' id='LC384'><span class="sd">      Traceback (most recent call last):</span></div><div class='line' id='LC385'><span class="sd">      ...</span></div><div class='line' id='LC386'><span class="sd">      RuntimeError: This batch request has already been sent</span></div><div class='line' id='LC387'><br/></div><div class='line' id='LC388'><span class="sd">    There is also a limit to the number of requests that can be sent in a single</span></div><div class='line' id='LC389'><span class="sd">    batch.  Going over this limit will cause an exception to be thrown.</span></div><div class='line' id='LC390'><br/></div><div class='line' id='LC391'><span class="sd">      &gt;&gt;&gt; batch = Batch()</span></div><div class='line' id='LC392'><span class="sd">      &gt;&gt;&gt; for i in xrange(BATCH_REQUEST_LIMIT+1):</span></div><div class='line' id='LC393'><span class="sd">      ...   batch.get(&#39;/me&#39;)</span></div><div class='line' id='LC394'><span class="sd">      Traceback (most recent call last):</span></div><div class='line' id='LC395'><span class="sd">      ...</span></div><div class='line' id='LC396'><span class="sd">      RuntimeError: You can&#39;t send more than 50 requests in a single batch</span></div><div class='line' id='LC397'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC398'><br/></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">client</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__api_calls</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__batch_request_sent</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC403'><br/></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__add_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__api_calls</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">BATCH_REQUEST_LIMIT</span><span class="p">:</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;You can&#39;t send more than </span><span class="si">%s</span><span class="s"> requests in a single batch&quot;</span> <span class="o">%</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">BATCH_REQUEST_LIMIT</span><span class="p">)</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__api_calls</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">ignore_result</span><span class="p">:</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">request</span></div><div class='line' id='LC413'><br/></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ignore_result</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__add_request</span><span class="p">(</span><span class="n">_GraphRequest</span><span class="p">(</span><span class="s">&#39;GET&#39;</span><span class="p">,</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">,</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span><span class="p">,</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore_result</span><span class="p">))</span></div><div class='line' id='LC420'><br/></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">post</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ignore_result</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__add_request</span><span class="p">(</span><span class="n">_GraphRequest</span><span class="p">(</span><span class="s">&#39;POST&#39;</span><span class="p">,</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">,</span></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span><span class="p">,</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore_result</span><span class="p">))</span></div><div class='line' id='LC427'><br/></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ignore_result</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__add_request</span><span class="p">(</span><span class="n">_GraphRequest</span><span class="p">(</span><span class="s">&#39;DELETE&#39;</span><span class="p">,</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">,</span></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span><span class="p">,</span></div><div class='line' id='LC433'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore_result</span><span class="p">))</span></div><div class='line' id='LC434'><br/></div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fql</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ignore_result</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__add_request</span><span class="p">(</span><span class="n">_GraphRequest</span><span class="p">(</span><span class="s">&#39;GET&#39;</span><span class="p">,</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;fql&#39;</span><span class="p">,</span></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&#39;q&#39;</span><span class="p">:</span> <span class="n">query</span><span class="p">},</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span><span class="p">,</span></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore_result</span><span class="p">))</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__build_params</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># See https://developers.facebook.com/docs/reference/api/batch/</span></div><div class='line' id='LC444'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># for documentation on how the batch api is supposed to work.</span></div><div class='line' id='LC445'><br/></div><div class='line' id='LC446'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">batch</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">all_files</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">request</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__api_calls</span><span class="p">:</span></div><div class='line' id='LC449'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;method&#39;</span><span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span><span class="p">}</span></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">request</span><span class="o">.</span><span class="n">ignore_result</span><span class="p">:</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;omit_response_on_success&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">name</span><span class="p">:</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">name</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="ow">in</span> <span class="p">[</span><span class="s">&#39;GET&#39;</span><span class="p">,</span> <span class="s">&#39;DELETE&#39;</span><span class="p">]:</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;relative_url&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">path</span><span class="o">+</span><span class="s">&#39;?&#39;</span><span class="o">+</span><span class="n">urlencode</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;relative_url&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">path</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">params</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span></div><div class='line' id='LC461'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">FileType</span><span class="p">):</span></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">all_files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;file</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">all_files</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;body&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">urlencode</span><span class="p">(</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC467'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="p">[</span><span class="s">&#39;attached_files&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">files</span><span class="p">)</span></div><div class='line' id='LC468'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">batch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">payload</span><span class="p">)</span></div><div class='line' id='LC469'><br/></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;batch&#39;</span><span class="p">:</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">batch</span><span class="p">)}</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">f</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">all_files</span><span class="p">):</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="s">&#39;file</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">f</span></div><div class='line' id='LC473'><br/></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">params</span></div><div class='line' id='LC475'><br/></div><div class='line' id='LC476'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">send</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__batch_request_sent</span><span class="p">:</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;This batch request has already been sent&quot;</span><span class="p">)</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__batch_request_sent</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC480'><br/></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="ow">or</span> <span class="n">_get_client</span><span class="p">()</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">responses</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__build_params</span><span class="p">())</span></div><div class='line' id='LC483'><br/></div><div class='line' id='LC484'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># process the response</span></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">request</span><span class="p">,</span> <span class="n">response</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__api_calls</span><span class="p">,</span> <span class="n">responses</span><span class="p">):</span></div><div class='line' id='LC486'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this happens when you use the result in a following request</span></div><div class='line' id='LC488'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">response</span><span class="p">[</span><span class="s">&#39;code&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">200</span><span class="p">:</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s">&#39;body&#39;</span><span class="p">])</span></div><div class='line' id='LC491'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request</span><span class="o">.</span><span class="n">error</span> <span class="o">=</span> <span class="n">ApiException</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s">&#39;body&#39;</span><span class="p">])[</span><span class="s">&#39;error&#39;</span><span class="p">])</span></div><div class='line' id='LC493'><br/></div><div class='line' id='LC494'><br/></div><div class='line' id='LC495'><span class="k">class</span> <span class="nc">Client</span><span class="p">:</span></div><div class='line' id='LC496'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;A class that encapsulates a client for a single access token.</span></div><div class='line' id='LC497'><br/></div><div class='line' id='LC498'><span class="sd">    Using a Client object, you can make requests using different access tokens</span></div><div class='line' id='LC499'><span class="sd">    within the same application.</span></div><div class='line' id='LC500'><br/></div><div class='line' id='LC501'><span class="sd">      &gt;&gt;&gt; user1 = Client(&#39;AAACjeiZB6FgIBAJhJMaspnA8V06q859FvUJsJtVbEsXpEKOv5H6RIvU7hWU5EgINj5fBPoGlVt0JIkWVYHVemOmehqMyiQFSWDbDq0AZDZD&#39;)</span></div><div class='line' id='LC502'><span class="sd">      &gt;&gt;&gt; user2 = Client(&#39;AAACjeiZB6FgIBAB8eZABg7So8ALDisFLugfIJSZCg3FEDRy82yEmdXYYfNvdv2kWVMWxaJgWqqVMPtG5v5n4lMG5VXmZBZBykQkeluhpFPQZDZD&#39;)</span></div><div class='line' id='LC503'><br/></div><div class='line' id='LC504'><span class="sd">      &gt;&gt;&gt; print user1.get(&#39;/me&#39;)[&#39;name&#39;]</span></div><div class='line' id='LC505'><span class="sd">      David Amcfbdajbbhi Alisonsen</span></div><div class='line' id='LC506'><span class="sd">      &gt;&gt;&gt; print user2.get(&#39;/me&#39;)[&#39;name&#39;]</span></div><div class='line' id='LC507'><span class="sd">      David Amcafiaddddh Yangstein</span></div><div class='line' id='LC508'><br/></div><div class='line' id='LC509'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC510'><br/></div><div class='line' id='LC511'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC512'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">access_token</span> <span class="o">=</span> <span class="n">access_token</span></div><div class='line' id='LC513'><br/></div><div class='line' id='LC514'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__get_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC515'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span> <span class="o">=</span> <span class="n">args</span> <span class="ow">or</span> <span class="p">{}</span></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">:</span></div><div class='line' id='LC517'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span><span class="p">[</span><span class="s">&#39;access_token&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span></div><div class='line' id='LC518'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subdomain</span> <span class="o">=</span> <span class="s">&#39;graph&#39;</span></div><div class='line' id='LC519'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;/videos&#39;</span> <span class="ow">in</span> <span class="n">path</span><span class="p">:</span></div><div class='line' id='LC520'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subdomain</span> <span class="o">=</span> <span class="s">&#39;graph-video&#39;</span></div><div class='line' id='LC521'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;access_token&#39;</span> <span class="ow">in</span> <span class="n">args</span> <span class="ow">or</span> <span class="s">&#39;client_secret&#39;</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">endpoint</span> <span class="o">=</span> <span class="s">&quot;https://</span><span class="si">%s</span><span class="s">.facebook.com&quot;</span> <span class="o">%</span> <span class="n">subdomain</span></div><div class='line' id='LC523'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC524'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">endpoint</span> <span class="o">=</span> <span class="s">&quot;http://</span><span class="si">%s</span><span class="s">.facebook.com&quot;</span> <span class="o">%</span> <span class="n">subdomain</span></div><div class='line' id='LC525'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">endpoint</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;?&#39;</span><span class="o">+</span><span class="n">urlencode</span><span class="p">(</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC526'><br/></div><div class='line' id='LC527'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC528'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_safe_json_load</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__get_url</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">params</span><span class="p">))</span></div><div class='line' id='LC529'><br/></div><div class='line' id='LC530'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">post</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC531'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="n">params</span> <span class="ow">or</span> <span class="p">{}</span></div><div class='line' id='LC532'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">poster_is_available</span><span class="p">:</span></div><div class='line' id='LC533'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span><span class="p">,</span> <span class="n">headers</span> <span class="o">=</span> <span class="n">poster</span><span class="o">.</span><span class="n">encode</span><span class="o">.</span><span class="n">multipart_encode</span><span class="p">(</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC534'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__get_url</span><span class="p">(</span><span class="n">path</span><span class="p">),</span> <span class="n">data</span><span class="p">,</span> <span class="n">headers</span><span class="p">)</span></div><div class='line' id='LC535'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_safe_json_load</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div><div class='line' id='LC536'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC537'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opener</span> <span class="o">=</span> <span class="n">build_opener</span><span class="p">(</span></div><div class='line' id='LC538'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">HTTPCookieProcessor</span><span class="p">(</span><span class="n">cookielib</span><span class="o">.</span><span class="n">CookieJar</span><span class="p">()),</span></div><div class='line' id='LC539'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_MultipartPostHandler</span><span class="p">)</span></div><div class='line' id='LC540'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC541'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">opener</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__get_url</span><span class="p">(</span><span class="n">path</span><span class="p">),</span> <span class="n">params</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">))</span></div><div class='line' id='LC542'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">HTTPError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC543'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error</span> <span class="o">=</span> <span class="n">_handle_http_error</span><span class="p">(</span><span class="n">e</span><span class="p">)</span></div><div class='line' id='LC544'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">error</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC547'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">params</span><span class="p">:</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC549'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="s">&#39;method&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;delete&#39;</span></div><div class='line' id='LC550'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">post</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span></div><div class='line' id='LC551'><br/></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fql</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">):</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__get_url</span><span class="p">(</span><span class="s">&#39;/fql&#39;</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;q&#39;</span><span class="p">:</span> <span class="n">query</span><span class="p">})</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_safe_json_load</span><span class="p">(</span><span class="n">url</span><span class="p">)[</span><span class="s">&#39;data&#39;</span><span class="p">]</span></div><div class='line' id='LC555'><br/></div><div class='line' id='LC556'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">graph_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC557'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__get_url</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC558'><br/></div><div class='line' id='LC559'><br/></div><div class='line' id='LC560'><span class="k">def</span> <span class="nf">_get_client</span><span class="p">():</span></div><div class='line' id='LC561'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">CLIENT</span></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">CLIENT</span> <span class="ow">or</span> <span class="n">CLIENT</span><span class="o">.</span><span class="n">access_token</span> <span class="o">!=</span> <span class="n">ACCESS_TOKEN</span><span class="p">:</span></div><div class='line' id='LC563'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">CLIENT</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">ACCESS_TOKEN</span><span class="p">)</span></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">CLIENT</span></div><div class='line' id='LC565'><br/></div><div class='line' id='LC566'><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC567'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Send a GET request to the graph api.</span></div><div class='line' id='LC568'><br/></div><div class='line' id='LC569'><span class="sd">    For example:</span></div><div class='line' id='LC570'><br/></div><div class='line' id='LC571'><span class="sd">      &gt;&gt;&gt; user = get(&#39;/me&#39;)</span></div><div class='line' id='LC572'><span class="sd">      &gt;&gt;&gt; print user[&#39;first_name&#39;]</span></div><div class='line' id='LC573'><span class="sd">      David</span></div><div class='line' id='LC574'><span class="sd">      &gt;&gt;&gt; short_user = get(&#39;/me&#39;, {&#39;fields&#39;:&#39;id,first_name&#39;})</span></div><div class='line' id='LC575'><span class="sd">      &gt;&gt;&gt; print short_user[&#39;id&#39;], short_user[&#39;first_name&#39;]</span></div><div class='line' id='LC576'><span class="sd">      100003169144448 David</span></div><div class='line' id='LC577'><br/></div><div class='line' id='LC578'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_client</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC580'><br/></div><div class='line' id='LC581'><span class="k">def</span> <span class="nf">iter_pages</span><span class="p">(</span><span class="n">json_response</span><span class="p">):</span></div><div class='line' id='LC582'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Iterate over multiple pages of data.</span></div><div class='line' id='LC583'><br/></div><div class='line' id='LC584'><span class="sd">    The graph api can return a lot of data, but will only return a limited</span></div><div class='line' id='LC585'><span class="sd">    amount of data in a single request.  To get more data, you must query for it</span></div><div class='line' id='LC586'><span class="sd">    explicitly using paging.  This function will do automatic paging in the form</span></div><div class='line' id='LC587'><span class="sd">    of an iterator.  For example to print the id of every photo tagged with the</span></div><div class='line' id='LC588'><span class="sd">    logged in user:</span></div><div class='line' id='LC589'><br/></div><div class='line' id='LC590'><span class="sd">      &gt;&gt;&gt; total = 0</span></div><div class='line' id='LC591'><span class="sd">      &gt;&gt;&gt; for photo in iter_pages(get(&#39;/19292868552/feed&#39;, {&#39;limit&#39;:2})):</span></div><div class='line' id='LC592'><span class="sd">      ...     total += 1</span></div><div class='line' id='LC593'><span class="sd">      ...     print &quot;There are at least&quot;, total, &quot;feed stories&quot;</span></div><div class='line' id='LC594'><span class="sd">      ...     if total &gt; 4: break</span></div><div class='line' id='LC595'><span class="sd">      There are at least 1 feed stories</span></div><div class='line' id='LC596'><span class="sd">      There are at least 2 feed stories</span></div><div class='line' id='LC597'><span class="sd">      There are at least 3 feed stories</span></div><div class='line' id='LC598'><span class="sd">      There are at least 4 feed stories</span></div><div class='line' id='LC599'><span class="sd">      There are at least 5 feed stories</span></div><div class='line' id='LC600'><br/></div><div class='line' id='LC601'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">json_response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;data&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)):</span></div><div class='line' id='LC603'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">json_response</span><span class="p">[</span><span class="s">&#39;data&#39;</span><span class="p">]:</span></div><div class='line' id='LC604'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">yield</span> <span class="n">item</span></div><div class='line' id='LC605'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">next_url</span> <span class="o">=</span> <span class="n">json_response</span><span class="p">[</span><span class="s">&#39;paging&#39;</span><span class="p">][</span><span class="s">&#39;next&#39;</span><span class="p">]</span></div><div class='line' id='LC606'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">json_response</span> <span class="o">=</span> <span class="n">_safe_json_load</span><span class="p">(</span><span class="n">next_url</span><span class="p">)</span></div><div class='line' id='LC607'><br/></div><div class='line' id='LC608'><span class="k">def</span> <span class="nf">post</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC609'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Send a POST request to the graph api.</span></div><div class='line' id='LC610'><br/></div><div class='line' id='LC611'><span class="sd">    You can also upload files using this function.  For example:</span></div><div class='line' id='LC612'><br/></div><div class='line' id='LC613'><span class="sd">      &gt;&gt;&gt; image = open(&quot;icon.gif&quot;, &quot;rb&quot;)</span></div><div class='line' id='LC614'><span class="sd">      &gt;&gt;&gt; photo_id = post(&#39;/me/photos&#39;,</span></div><div class='line' id='LC615'><span class="sd">      ...            {&#39;name&#39;: &#39;My Photo&#39;,</span></div><div class='line' id='LC616'><span class="sd">      ...             &#39;source&#39;: image})[&#39;id&#39;]</span></div><div class='line' id='LC617'><span class="sd">      &gt;&gt;&gt; image.close()</span></div><div class='line' id='LC618'><span class="sd">      &gt;&gt;&gt; print get(&#39;/&#39;+photo_id)[&#39;name&#39;]</span></div><div class='line' id='LC619'><span class="sd">      My Photo</span></div><div class='line' id='LC620'><br/></div><div class='line' id='LC621'><span class="sd">    Or like an object:</span></div><div class='line' id='LC622'><br/></div><div class='line' id='LC623'><span class="sd">      &gt;&gt;&gt; success = post(&#39;/&#39;+photo_id+&#39;/likes&#39;)</span></div><div class='line' id='LC624'><span class="sd">      &gt;&gt;&gt; print get(&#39;/&#39;+photo_id+&#39;/likes&#39;)[&#39;data&#39;][0][&#39;name&#39;]</span></div><div class='line' id='LC625'><span class="sd">      David Amcafiaddddh Yangstein</span></div><div class='line' id='LC626'><br/></div><div class='line' id='LC627'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC628'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_client</span><span class="p">()</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC629'><br/></div><div class='line' id='LC630'><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC631'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Send a DELETE request to the graph api.</span></div><div class='line' id='LC632'><br/></div><div class='line' id='LC633'><span class="sd">    For example:</span></div><div class='line' id='LC634'><br/></div><div class='line' id='LC635'><span class="sd">      &gt;&gt;&gt; msg_id = post(&#39;/me/feed&#39;, {&#39;message&#39;:&#39;hello world&#39;})[&#39;id&#39;]</span></div><div class='line' id='LC636'><span class="sd">      &gt;&gt;&gt; delete(&#39;/&#39;+msg_id)</span></div><div class='line' id='LC637'><span class="sd">      True</span></div><div class='line' id='LC638'><br/></div><div class='line' id='LC639'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC640'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_client</span><span class="p">()</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC641'><br/></div><div class='line' id='LC642'><span class="k">def</span> <span class="nf">fql</span><span class="p">(</span><span class="n">query</span><span class="p">):</span></div><div class='line' id='LC643'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Make an fql request.</span></div><div class='line' id='LC644'><br/></div><div class='line' id='LC645'><span class="sd">    For example:</span></div><div class='line' id='LC646'><br/></div><div class='line' id='LC647'><span class="sd">      &gt;&gt;&gt; data = fql(&#39;SELECT name FROM user WHERE uid = me()&#39;)</span></div><div class='line' id='LC648'><span class="sd">      &gt;&gt;&gt; print data[0][&#39;name&#39;]</span></div><div class='line' id='LC649'><span class="sd">      David Amcafiaddddh Yangstein</span></div><div class='line' id='LC650'><br/></div><div class='line' id='LC651'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC652'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_client</span><span class="p">()</span><span class="o">.</span><span class="n">fql</span><span class="p">(</span><span class="n">query</span><span class="p">)</span></div><div class='line' id='LC653'><br/></div><div class='line' id='LC654'><span class="k">def</span> <span class="nf">graph_url</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC655'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get the full url to the graph api for the given path and query args.</span></div><div class='line' id='LC656'><br/></div><div class='line' id='LC657'><span class="sd">    This is useful if you want to use your own method of making http requests or</span></div><div class='line' id='LC658'><span class="sd">    are not interested in the json parsing that occurs by default. For example,</span></div><div class='line' id='LC659'><span class="sd">    download a large profile picture of Mark Zuckerberg:</span></div><div class='line' id='LC660'><br/></div><div class='line' id='LC661'><span class="sd">      &gt;&gt;&gt; url = graph_url(&#39;/zuck/picture&#39;, {&quot;type&quot;:&quot;large&quot;})</span></div><div class='line' id='LC662'><span class="sd">      &gt;&gt;&gt; filename, response = urllib.urlretrieve(url, &#39;mark.jpg&#39;)</span></div><div class='line' id='LC663'><br/></div><div class='line' id='LC664'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC665'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">_get_client</span><span class="p">()</span><span class="o">.</span><span class="n">graph_url</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC666'><br/></div><div class='line' id='LC667'><span class="k">def</span> <span class="nf">oauth_url</span><span class="p">(</span><span class="n">app_id</span><span class="p">,</span> <span class="n">redirect_uri</span><span class="p">,</span> <span class="n">auth_scope</span><span class="p">):</span></div><div class='line' id='LC668'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Generates a url to an oath authentication dialog.</span></div><div class='line' id='LC669'><br/></div><div class='line' id='LC670'><span class="sd">      &gt;&gt;&gt; print oauth_url(APP_ID, &#39;http://127.0.0.1:8080/&#39;, [&#39;publish_stream&#39;])</span></div><div class='line' id='LC671'><span class="sd">      https://www.facebook.com/dialog/oauth?scope=publish_stream&amp;redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2F&amp;response_type=token&amp;client_id=179745182062082</span></div><div class='line' id='LC672'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC673'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;https://www.facebook.com/dialog/oauth?&#39;</span> <span class="o">+</span> \</div><div class='line' id='LC674'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">urlencode</span><span class="p">({</span><span class="s">&#39;client_id&#39;</span><span class="p">:</span><span class="n">app_id</span><span class="p">,</span></div><div class='line' id='LC675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;redirect_uri&#39;</span><span class="p">:</span><span class="n">redirect_uri</span><span class="p">,</span></div><div class='line' id='LC676'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;response_type&#39;</span><span class="p">:</span><span class="s">&#39;token&#39;</span><span class="p">,</span></div><div class='line' id='LC677'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;scope&#39;</span><span class="p">:</span><span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">auth_scope</span><span class="p">)})</span></div><div class='line' id='LC678'><br/></div><div class='line' id='LC679'><br/></div><div class='line' id='LC680'><span class="n">INTRO_MESSAGE</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span><span class="se">\</span></div><div class='line' id='LC681'><span class="s">  __ _                                _</span></div><div class='line' id='LC682'><span class="s"> / _| |                              | |</span></div><div class='line' id='LC683'><span class="s">| |_| |__   ___  ___  _ __  ___  ___ | | ___</span></div><div class='line' id='LC684'><span class="s">|  _| &#39;_ \ / __|/ _ \| &#39;_ \/ __|/ _ \| |/ _ </span><span class="se">\\</span><span class="s"></span></div><div class='line' id='LC685'><span class="s">| | | |_) | (__| (_) | | | \__ \ (_) | |  __/</span></div><div class='line' id='LC686'><span class="s">|_| |_.__/ \___|\___/|_| |_|___/\___/|_|\___|</span></div><div class='line' id='LC687'><br/></div><div class='line' id='LC688'><span class="s">Type help() for a list of commands.</span></div><div class='line' id='LC689'><span class="s">quick start:</span></div><div class='line' id='LC690'><br/></div><div class='line' id='LC691'><span class="s">  &gt;&gt;&gt; authenticate()</span></div><div class='line' id='LC692'><span class="s">  &gt;&gt;&gt; print &quot;Hello&quot;, get(&#39;/me&#39;)[&#39;name&#39;]</span></div><div class='line' id='LC693'><br/></div><div class='line' id='LC694'><span class="s">&#39;&#39;&#39;</span></div><div class='line' id='LC695'><br/></div><div class='line' id='LC696'><span class="k">def</span> <span class="nf">shell</span><span class="p">():</span></div><div class='line' id='LC697'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC698'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">IPython.Shell</span> <span class="kn">import</span> <span class="n">IPShellEmbed</span></div><div class='line' id='LC699'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">IPShellEmbed</span><span class="p">()(</span><span class="n">INTRO_MESSAGE</span><span class="p">)</span></div><div class='line' id='LC700'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">code</span></div><div class='line' id='LC702'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">code</span><span class="o">.</span><span class="n">InteractiveConsole</span><span class="p">(</span><span class="nb">globals</span><span class="p">())</span><span class="o">.</span><span class="n">interact</span><span class="p">(</span><span class="n">INTRO_MESSAGE</span><span class="p">)</span></div><div class='line' id='LC703'><br/></div><div class='line' id='LC704'><br/></div><div class='line' id='LC705'><span class="k">def</span> <span class="nf">test_suite</span><span class="p">():</span></div><div class='line' id='LC706'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">doctest</span></div><div class='line' id='LC707'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">ACCESS_TOKEN</span></div><div class='line' id='LC708'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ACCESS_TOKEN</span> <span class="o">=</span> <span class="s">&#39;AAACjeiZB6FgIBAB8eZABg7So8ALDisFLugfIJSZCg3FEDRy82yEmdXYYfNvdv2kWVMWxaJgWqqVMPtG5v5n4lMG5VXmZBZBykQkeluhpFPQZDZD&#39;</span></div><div class='line' id='LC709'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">doctest</span><span class="o">.</span><span class="n">DocTestSuite</span><span class="p">()</span></div><div class='line' id='LC710'><br/></div><div class='line' id='LC711'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC712'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shell</span><span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading large-loading-area" style="display:none;" data-tree-list-url="/facebook/fbconsole/tree-list/8d66505c6c6a9689b29c677ddc81899ca19bb5ec" data-blob-url-prefix="/facebook/fbconsole/blob/8d66505c6c6a9689b29c677ddc81899ca19bb5ec">
  <img src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-64.gif?1329872009" height="64" width="64">
</div>

        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer" >
        
  <div class="upper_footer">
     <div class="container clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://enterprise.github.com/">GitHub Enterprise</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Clients</h4>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://windows.github.com/">GitHub for Windows</a></li>
         <li><a href="http://eclipse.github.com/">GitHub for Eclipse</a></li>
         <li><a href="http://mobile.github.com/">GitHub Mobile Apps</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://get.gaug.es/">Gauges: Web analytics</a></li>
         <li><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></li>
         <li><a href="https://gist.github.com">Gist: Code snippets</a></li>

         <h4 class="second">Extras</h4>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="container clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
          <li><a href="https://github.com/site/terms">Terms of Service</a></li>
          <li><a href="https://github.com/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2012 <span title="0.29904s from fe5.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspaces_logo.png?1329521041" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

      </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
        <dd>Submit comment</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first">
        <h3>Browsing Commits</h3>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>escape</dt>
          <dd>Close form</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>p</dt>
          <dd>Parent commit</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o</dt>
          <dd>Other parent commit</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div id="ajax-error-message">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="ajax-error-dismiss">Dismiss</a>
    </div>

    <div id="logo-popup">
      <h2>Looking for the GitHub logo?</h2>
      <ul>
        <li>
          <h4>GitHub Logo</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip"><img alt="Github_logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/github_logo.png?1306884369" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip" class="minibutton btn-download download">Download</a>
        </li>
        <li>
          <h4>The Octocat</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip"><img alt="Octocat" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/octocat.png?1306884369" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip" class="minibutton btn-download download">Download</a>
        </li>
      </ul>
    </div>

    
    <span id='server_response_time' data-time='0.30137' data-host='fe5'></span>
  </body>
</html>

